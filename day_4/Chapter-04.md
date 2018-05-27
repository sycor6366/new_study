# 第四天
##  Django介绍
Django是一个高级Python Web框架，鼓励快速开发和实用的设计。
由经验丰富的开发人员开发，它可以处理Web开发的大部分问题，
因此可以专注于编写应用程序，而无需重新发明轮子。

Django 特点
1.  快速: Django旨在帮助开发人员尽可能快地完成应用程序
2.  安全: Django严肃对待安全并帮助开发人员避免许多常见的安全错误
3.  可伸缩:  Django快速灵活扩展的能力
4.  丰富的组件: Django 内置各种web开发常用功能组件

## Django安装
使用pycharm安装Django
File=>Setting=>Project:项目名=>Project Interpreter=>点击右侧+号= >在搜索框输入django=> 在列表中选中django=>点击install

使用pip
````
pip install django
````

验证django
````
>>> import django
>>> django.get_version()
'2.0.5'

````

## 创建一个项目

在pycharm Terminal中输入
````
django-admin startproject mysite
````

项目结构
````
└── mysite
    ├── manage.py
    └── mysite
        ├── __init__.py
        ├── settings.py
        ├── urls.py
        └── wsgi.py

````
+ 顶部mysite:  项目根目录。 它的名字与Django无关; 你可以将它重命名为任何你喜欢的名字
+ manager.py: 一个命令行实用程序，可让您以各种方式与此Django项目进行交互。
+ 内部mysite: 项目的实际Python包。 它的名字是你需要用来导入任何东西的Python包名
+ mysite/__init__.py: 一个空文件，告诉Python这个目录应该被视为一个Python包
+ mysite/settings.py:  这个Django项目的配置文件
+ mysite/urls.py:  这个Django项目的URL声明
+ mysite/wsgi.py:  WSGI兼容的Web服务器,为项目提供服务的入口点

以开发模式运行服务器

````
cd mysite
python manage.py runserver
````

访问django项目
在浏览器打开http://127.0.0.1:8000

修改开发服务器默认端口
````
d mysite
ython manage.py runserver 8080
````

默认开发服务器监听127.0.0.1
修改监听ip
````
python manage.py runserver 0:8000
````

## 创建第一个app
项目和应用程序有什么区别？ 应用程序是一种Web应用程序，它可以执行某些操作，
例如博客系统，公共记录数据库或简单的民意调查应用程序。 
项目是特定网站的配置和应用程序的集合。 项目可以包含多个应用程序。

````
python manage.py startapp myapp
````

myapp目录结构

````
myapp
├── admin.py
├── apps.py
├── __init__.py
├── migrations
│   └── __init__.py
├── models.py
├── tests.py
└── views.py
````

admin.py  将models注册到djangoadmin
apps.py  app 配置
__init__.py  表明该文件夹为包
migrations  数据库版本升级
models.py 数据库管理
tests.py  测试文件
views  视图文件

编辑myapp/views.py
````

````

创建myapp/urls.py

````
from django.urls import path

from .  import views


urlpatterns = [
    path('', views.index, name='index')
]

````
编辑mysite/urls.py

````
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', include('myapp.urls'))
]
````

path 函数定义了4个参数， 两个必须的，route和view，两个可选的name和kwargs

**path()参数 route**

路由是一个包含URL模式的字符串。处理请求时，Django从urlpatterns中的第一个模式开始，
并在列表中向下，并将请求的URL与每个模式进行比较，直到找到匹配的模式。
不搜索GET和POST参数或域名。
例如，在https://www.example.com/myapp/的请求中，URLconf将查找myapp/。
 在https://www.example.com/myapp/?page=3的请求中，URLconf也会查找myapp/。
 
**path() 参数view**
当Django找到匹配的模式时，它将HttpRequest对象作为第一个参数，并
将路由中的任何“捕获”值作为关键字参数调用指定的视图函数。
 
**patch() 参数name**
 
命名URL可以让你从Django其他地方明确地引用它，特别是在模板中


## 数据库配置

mysite/settings.py。这是一个ython模块，用于Django配置


默认情况下，配置使用SQLite。如果你是数据库新手，或者你只是想尝试Django，这是最简单的选择
SQLite包含在Python中，所以你不需要安装其他任何东西来支持你的数据库，
然而，当开始你的第一个真正的项目时，你可能想要使用像MySQL这样的更具可扩展性的数据库。
如果您想使用其他数据库，请安装适当的数据库绑定，并在DATABASES的default项中更改以下键以匹配数据库连接

+ ENGINE: 可用的配置有'django.db.backends.sqlite3', 'django.db.backends.postgresql', 'django.db.backends.mysql', 
'django.db.backends.oracle' 等
+ NAME: 数据库的名称
+ HOST: 数据库主机名
+ USER: 数据库用户名
+ PASSWORD: 数据库密码

### 创建 models

模型 - 数据库布局以及其他元数据

在我们的app里我们将创建两个models:   Question 和 Choice
Question 包含一个问题和创建问题的时间
Choice 包含一个选项和选项的的票数
每个Choice都和一个Question关联

Models 通过python类来定义，编辑文件myapp/models.py

````
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
````
代码很简单。每个模型都由代表django.db.models.Model的子类表示。
每个模型都有许多类变量，每个变量表示模型中的数据库字段。

每个字段由一个Field类的实例表示 - 例如，字符字段的CharField和日期时间的DateTimeField。
这告诉Django每个字段拥有什么类型的数据。

每个Field实例的名称（例如question_text或pub_date）是机器友好格式的字段名称。
你将在你的Python代码中使用此值，并且你的数据库将使用它作为列名称。

你可以使用字段的可选第一个位置参数来指定一个人类可读的名称，
在这个例子中，我们只为Question.pub_date定义了一个人类可读的名字

某些Field类需要参数。例如，CharField要求你给它一个max_length，
字段还可以通过default参数设置默认值如例子中的votes字段默认值为0

最后，请注意使用ForeignKey定义的关系。这告诉Django每个Choice都与单个 Question有关。 
Django支持所有常见的数据库关系：多对一，多对多和一对一

### 应用models

这一小部分模型代码为Django提供了大量信息。有了它，Django能够
+ 为此应用程序创建数据库模式（CREATE TABLE语句）
+ 创建一个用于访问Question和Choice对象的Python数据库访问API

但首先我们需要告诉我们的项目，myapp应用程序已安装

打开mysite/settings.py，INSTALLED_APPS设置如下：
````
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
````
默认情况下，INSTALLED_APPS包含以下应用程序，所有这些应用程序都与Django一起提供
+ django.contrib.admin - 管理网站
+ django.contrib.auth - 一个认证系统。
+ django.contrib.contenttypes - 内容类型的框架。
+ django.contrib.sessions - 会话框架
+ django.contrib.messages - 一个消息框架。
+ django.contrib.staticfiles - 管理静态文件的框架。

其中一些应用程序至少使用了一个数据库表，所以我们需要在数据库中创建表格，
然后才能使用它们。为此，请运行以下命令
````
python manage.py migrate

# 返回内容
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying sessions.0001_initial... OK
````


编辑我们的mysite/settings.py，我们需要在INSTALLED_APPS设置中添加对其配置类的引用
MyappConfig类位于myapp/apps.py文件中，因此它的相对路径是'myapp.apps.PollsConfig'

````
INSTALLED_APPS = [
    'myapp.apps.MyappConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
````


现在Django知道myapp应用程序。让我们运行另一个命令
````
python manage.py makemigrations myapp

# 返回内容
Migrations for 'myapp':
  myapp\migrations\0001_initial.py
    - Create model Choice
    - Create model Question
    - Add field question to choice

````

通过运行makemigrations，您告诉Django你已经对模型进行了一些更改，
并且希望将这些更改存储为migrations。

migrations是Django如何将更改变更到数据库 - 它们只是磁盘上的文件
如果你喜欢，你可以阅读新模型的migrations;myapp/migrations/0001_initial.py

有一个命令可以为你运行migrationgs并自动管理你的数据库- 这就是所谓的migrate
我们稍后会介绍它 - 但首先，我们来看看migrate过程将运行的SQL。 
sqlmigrate命令使用migration 名称并返回它们的SQL：

````
python manage.py sqlmigrate myapp 0001

# 返回
BEGIN;
--
-- Create model Choice
--
CREATE TABLE "myapp_choice" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "choice_text" varchar(200) NOT NULL, "votes" integer NOT NULL);
--
-- Create model Question
--
CREATE TABLE "myapp_question" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "question_text" varchar(200) NOT NULL, "pub_date" datetime NOT NULL);
--
-- Add field question to choice
--
ALTER TABLE "myapp_choice" RENAME TO "myapp_choice__old";
CREATE TABLE "myapp_choice" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "choice_text" varchar(200) NOT NULL, "votes" integer NOT NULL, "question_id" integer
 NOT NULL REFERENCES "myapp_question" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "myapp_choice" ("id", "choice_text", "votes", "question_id") SELECT "id", "choice_text", "votes", NULL FROM "myapp_choice__old";
DROP TABLE "myapp_choice__old";
CREATE INDEX "myapp_choice_question_id_6149fbd4" ON "myapp_choice" ("question_id");
COMMIT;

````

+ 输出取决于不通的数据库，我们现在是默认的sqllite
+ 表名是通过组合应用程序的名称（myapp）和模型的小写名称（question，choice自动生成的
+ 主键（ID）会自动添加
+ 按照惯例，Django将“_id”附加到外键字段名称
+ sqlmigrate命令实际上不会对数据库做任何操作，只是输出migrations中包含的SQL语句

现在执行migrate

````
python manage.py migrate

# 返回内容
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, myapp, sessions
Running migrations:
  Applying myapp.0001_initial... OK
  
````

migrate命令会应用所有尚未应用的migrations，本质上是将你对模型所做的更改与数据库同步

migrations功能非常强大，您可以随着时间的推移更改模型，
而无需删除数据库或表格并创建新的数据库，专门用于实时升级数据库，而不会丢失数据

请记住进行数据库更改三步
+ 更改你的models（models.py）
+ 执行python manage.py makemigrations 为这些更改创建migrations
+ 执行 python manage.py migrate 应用变更到数据库

### 数据库api

现在，让我们使用交互式Python shell。要调用Python shell，请使用以下命令
````
python manage.py shell
# 返回内容
Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>>

>>> from myapp.models import Choice, Question  # 导入我们的模型类
>>> Question.objects.all() # 查询question表，现在还没有内容
<QuerySet []>
# 插入一条记录
>>> from django.utils import timezone
>>> q = Question(question_text="What's new?", pub_date=timezone.now())
>>> q.save()
>>> q.id
1
>>> q.question_text
"What's new?"
>>> q.pub_date
datetime.datetime(2018, 5, 20, 5, 41, 9, 912096, tzinfo=<UTC>)
# 修改字段的值
>>> q.question_text = "What's up?"
>>> q.save()
>>> Question.objects.all()
<QuerySet [<Question: Question object (1)>]>
````
<Question: Question object (1)>  这是个什么鬼？完全不可读
让我们通过编辑myapp/models.py文件，将__str __（）方法添加到Question和Choice中来解决这个问题
````
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
````

再次打开shell
````
>>> from myapp.models import Choice, Question
>>> Question.objects.all()
<QuerySet [<Question: What's up?>]>
# Django提供了完全由关键字参数驱动的丰富的数据库查找API
>>> Question.objects.filter(id=1)
<QuerySet [<Question: What's up?>]>
>>> from django.utils import timezone
>>> current_year = timezone.now().year
>>> Question.objects.get(pub_date__year=current_year) #只有一条记录是才能使用get
<Question: What's up> 
# 如果记录不存在get放回异常
>>> Question.objects.get(id=2)
...
myapp.models.DoesNotExist: Question matching query does not exist.

# 通过主键查找是最常见的情况
# 以下内容与Question.objects.get(id = 1)相同
>>> q = Question.objects.get(pk=1)
>>> q.question_text
"What's up"
# 显示相关对象集（Choice）中的所有记录 - 目前为止没有
>>> q.choice_set.all()
<QuerySet []>
# 创建三个选项
>>> q.choice_set.create(choice_text='Not much', votes=0)
<Choice: Not much>
>>> q.choice_set.create(choice_text='The sky', votes=0)
<Choice: The sky>
>>> c = q.choice_set.create(choice_text='Just hacking again', votes=0)
# 选项所关联的问题
>>> c.question
<Question: What's up>
# 问题所有的选项
>>> q.choice_set.all()
<QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>
>>> q.choice_set.count()
3
Choice.objects.filter(question__pub_date__year=current_year)
>>> c = q.choice_set.filter(choice_text__startswith='Just hacking')
>>> c.delete()
(1, {'myapp.Choice': 1})
````

### djnago admin

创建一个管理员用户
````
 python manage.py createsuperuser
````

启动开发服务器
````
python manage.py runserver
````
在浏览器输入http://127.0.0.1/admin

**使admin可以修改myapp的数据**

只需做一件事：我们需要告诉管理员Question对象具有管理界面。
要做到这一点，打开polls / admin.py文件，并编辑
````
from django.contrib import admin

from .models import Question

admin.site.register(Question)

````
然后刷新浏览器页面，就可以看到Question
![image](./Chapter-04-code/pics/admin-1.jpg)
点击Question,现在你在“更改列表”页面。
此页面显示数据库中的所有问题，并让你选择一个来更改
![image](./Chapter-04-code/pics/admin-2.jpg)
点击“What's up？”来编辑它
![image](./Chapter-04-code/pics/admin-3.jpg)

+ 表单是从Question模型自动生成的
+ 不同的模型字段类型（DateTimeField，CharField）对应于相应的HTML输入小部件。
每种类型的领域都知道如何在Django管理中显示自己










