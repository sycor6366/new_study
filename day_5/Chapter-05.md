第五天
myapp 视图概览
在我们的应用程序中，我们将拥有以下四个视图

index页面 - 显示最新的几个问题
detail页面 - 显示问题，没有结果，但有选择的表单
result页面 - 显示特定问题的结果
vote 页面 - 对特定的问题的投票进行处理
在Django中，网页和其他内容由视图传递，每个视图都由一个简单的Python函数（或基于类的视图的方法）表示 Django将通过检查请求的URL（准确地说，域名后的URL部分）来选择一个视图。 在网络上，可能会遇到诸如此类的url“ME2/Sites/dirmod.asp?sid=&type=gen&mod=Core+Pages&gid=A6CD4967199A42D9B65B1B Django允许我们使用更优雅的方式 URL，只是URL的一般形式 如/newsarchive/2018/06/.

为了从URL获得视图，Django使用了'URLconf'（urls.py）。 URLconf将URL模式映射到视图

添加views
现在让我们再添加一些视图到myapp/views.py。这些视图与我们第一index，略有不同 它们有参数

from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("Hello, world, You're at myapp index")


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
修改myapp/urls.py的path来调用这些views

from django.urls import path

from .  import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /myapp/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /myapp/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
在浏览器输入"http://127.0.0.1:8000/myapp/1/"，将运行detail（）方法并显示你在URL中提供的任何ID。 尝试“http://127.0.0.1:8000/myapp/1/results/”和“http://127.0.0.1:8000/myapp/1/vote/” - 这些将显示结果和投票页面。 当有人从你的网站请求一个页面 - 比如说“http://127.0.0.1:8000/myapp/1/”时，Django将加载mysite.urls 模块(setting中的ROOT_URLCONF配置的） 它找到名为urlpatterns的变量并按顺序遍历这些模式,在'myapp/'找到匹配项后，它会去掉匹配的文本（“myapp/”）， 并将剩余的文本“1/”发送到“myapp.urls” 以供进一步处理,在那里匹配'<int：question_id>/'，调用detail（）视图，如下所示：

detail(request=<HttpRequest object>, question_id=1)
question_id=1部分来自<int：question_id>。使用尖括号“捕获”部分URL并将其作为关键字参数发送到视图函数。 该字符串的：question_id>部分定义将用于标识匹配模式的名称,并且<int：部分是一个转换器，它决定了哪些模式应该匹配这部分URL路径。

编写有用view
每个视图负责执行以下两项操作之一：返回包含所请求页面内容的HttpResponse对象，或引发异常（如Http404） 视图可以从数据库中读取记录，可以使用模板系统，可以生产html,json,xml,zip,pdf 等等 以下是一个新的index（）视图，它显示了系统中最新的5个轮询问题，用逗号分隔：

from django.http import HttpResponse
# Create your views here.

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

但这里有一个问题：页面的设计在视图中是硬编码的。 如果你想改变页面的内容，你必须编辑这个Python代码 因此，让我们使用Django的模板系统，将python代码和页面内容分离

首先，在myapp目录中创建一个名为templates的目录。 Django将在那里寻找模板。 mysite/settings.py中的TEMPLATES设置了Django如何加载和渲染模板。默认设置模板系统为DjangoTemplates， 且'APP_DIRS': True, 按照惯例，DjangoTemplates在INSTALLED_APPS中查找“templates”子目录。 在myapp/templates 目录中创建一个目录为myapp，在myapp/templates/myapp 中创建一个文件叫index.html

{% if latest_question_list %}
    <ul>
    {% for question in latest_question_list %}
        <li><a href="/myapp/{{ question.id }}/">{{ question.question_text }}</a></li>
    {% endfor %}
    </ul>
{% else %}
    <p>No polls are available.</p>
{% endif %}

现在让我们更新我们的myapp/views.py中的索引视图以使用模板：

from django.http import HttpResponse
# Create your views here.
from django.template import loader
from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('myapp/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))


该代码加载名为myapp/index.html的模板并将其传递给上下文，上下文是一个将模板变量名称映射到Python对象的字典

快捷方式 render()

from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render
from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'myapp/index.html', context)

render() 函数将请求对象作为第一个参数，将模板名称作为第二个参数，将字典作为其可选的第三个参数。 它返回给定上下文呈现给定模板的HttpResponse对象。

定义404 error
编写detail页面

from django.http import HttpResponse
# Create your views here.
from django.http import Http404
from django.shortcuts import render
from .models import Question




def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'myapp/detail.html', {'question': question})



如果所请求的ID的问题不存在，该视图会引发Http404异常

编写myapp/detail.html模板

{{ question }}
输入存在的id http://127.0.0.1:8000/myapp/1/ 输入不存在的id http://127.0.0.1:8000/myapp/100/

快捷方式 get_object_or_404()

from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Question




def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})



get_object_or_404（）函数将Django model class作为其第一个参数和任意数量的关键字参数传递给模型管理器的get（）函数 如果对象不存在，它会引发Http404。

还有一个get_list_or_404（）函数，它的作用与get_object_or_404（）一样, 除了使用filter（）而不是get（）。 如果列表为空，它会引发Http404。

再次编辑detail模板

<h1>{{ question.question_text }}</h1>
<ul>
{% for choice in question.choice_set.all %}
    <li>{{ choice.choice_text }}</li>
{% endfor %}
</ul>
模板系统使用 点查找 语法来访问变量属性,比如{{ question.question_text }} 方法调用发生在{％for％}循环中：question.choice_set.all被解释为Python代码question.choice_set.all() 它返回Choice对象的迭代并适用于{％for％}标记。

移除模板中的url硬编码
回到myapp/index.html 模板

包含如下url硬编码

<li><a href="/myapp/{{ question.id }}/">{{ question.question_text }}</a></li>
这种硬编码，紧密耦合的方法存在的问题是，在具有大量模板的项目上更改网址变得非常具有挑战性。 但是，由于在myapp.urls模块的path()函数中定义了name参数，因此可以使用{％url％}模板标记删除对URL配置中定义的特定URL路径的依赖：

<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
它的工作方式是查找myapp.urls模块中指定的URL定义,如果想改变url只需改变myapp.urls path的模式

编写一个表单
myapp/detail.html

<h1>{{ question.question_text }}</h1>

{% if error_message %}<p><strong>{{ error_message }}</strong></p>{% endif %}

<form action="{% url 'vote' question.id %}" method="post">
{% csrf_token %}
{% for choice in question.choice_set.all %}
    <input type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{ choice.id }}" />
    <label for="choice{{ forloop.counter }}">{{ choice.choice_text }}</label><br />
{% endfor %}
<input type="submit" value="Vote" />
</form>
上面的模板为每个问题选项显示一个单选按钮，每个单选按钮的值是关联的问题选项的ID，每个单选按钮的name是“choice” 这意味着，当有人选择其中一个单选按钮并提交表单时，它会发送POST数据为所选选项的ID。这是HTML表单的基本概念

我们将表单的action设置为{％url'vote'question.id％} method为post，即使用post方法想该url提交数据

forloop.counter表示for标签经过循环的次数

由于我们正在创建POST表单（可能会影响修改数据），因此我们需要担心跨站点请求伪造，Django带有一个非常易用的系统来防止它。 简而言之，所有面向内部URL的POST表单都应使用{％csrf_token％}模板标记

现在，让我们创建一个处理提交数据的Django视图，并对其进行处理。

myapp/views.py:

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Choice, Question
# ...
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'myapp/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('results', args=(question.id,)))
request.POST是一个类似字典的对象，允许你通过键名访问提交的数据。 在这种情况下，request.POST['choice']返回所选选项的ID。 请注意，Django还提供request.GET以相同的方式访问GET数据 但我们明确在代码中使用了request.POST，以确保数据仅通过POST调用进行更改。

如果在POST数据中未提供选项，request.POST['choice']将引发KeyError。 上面的代码检查KeyError并重新显示带有错误消息的问题表单，如果没有给出选择

增加选择计数后，代码返回HttpResponseRedirect而不是正常的HttpResponse。 HttpResponseRedirect接受一个参数,参数为用户将被重定向到的URL

在本例中，我们在HttpResponseRedirect构造函数中使用reverse()函数。此功能有助于避免在视图功能中硬编码URL 它给出了我们想要传递控制权的视图的url模式的名称以及URL模式的可变部分

接下来编写result视图

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'myapp/results.html', {'question': question})
编写myapp/results.html模板

<h1>{{ question.question_text }}</h1>

<ul>
{% for choice in question.choice_set.all %}
    <li>{{ choice.choice_text }} -- {{ choice.votes }} vote{{ choice.votes|pluralize }}</li>
{% endfor %}
</ul>

<a href="{% url 'detail' question.id %}">Vote again?</a>
通用视图
detail(),results(),index()这些视图代表了基本Web开发的常见案例， 根据URL中传递的参数从数据库获取数据，加载模板并返回呈现的模板。 由于这很常见，Django提供了一个称为“通用视图”的功能

我们将我们的投票应用程序转换为使用通用视图系统，以便我们可以删除一大堆我们自己的代码。 我们只需采取几个步骤即可完成转换。

修改URLconf
删除一些旧的不需要的视图
基于Django通用视图引入新的视图
修改URLconf

from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
修改view

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'myapp/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'myapp/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'myapp/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'myap/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('results', args=(question.id,)))
我们在这里使用两个通用视图：ListView和DetailView。 这两个视图分别抽象出“显示对象列表”和“显示特定类型对象的详细页面”的概念

每个通用视图都需要知道它将采取何种model。 这是使用model属性提供的
他DetailView通用视图期望从URL捕获的主键值被称为“pk”，所以我们已经改变了通用视图的question_id为pk。
默认情况下，DetailView通用视图使用名为/ _detail.html的模板。 在我们的例子中，它会使用模板“myapp/question_detail.html”.template_name属性用于告诉Django使用特定的模板名称而不是自动生成的默认模板名称。 在前面的例子，模板已经提供了一个包含question和latest_question_list上下文变量的上下文。 对于DetailView，问题变量是自动提供的 - 由于我们使用Django 的model（Question），Django能够为上下文变量确定合适的名称 但是，对于ListView，自动生成的上下文变量是question_list。为了覆盖这个，我们提供context_object_name属性，指定我们想用latest_question_list来代替。