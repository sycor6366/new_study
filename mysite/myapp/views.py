from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
# Create your views here.
from django.template import loader
from django.http import Http404
from django.shortcuts import render,get_object_or_404
from .models import  Question,Choicd
from django.views import generic


# def index(request) :
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('myapp/index.html')
#     context = {
#         'latest_question_list':latest_question_list
#     }
#     # return HttpResponse(template.render(context,request))
#     return render(request,'myapp/index.html',context)
# def detail(request,question_id):
#     question = get_object_or_404(Question,pk = question_id)
#     return render(request,'myapp/detail.html',{'question':question})
#
# def results(request,question_id):
#     question = get_object_or_404(Question,pk=question_id)
#     return  render(request,'myapp/results.html',{'question':question})
#
# def vote(request,question_id):
#     question = get_object_or_404(Question,pk = question_id)
#     try:
#         selected_choice = question.choicd_set.get(pk=request.POST['choice'])
#     except (KeyError,Choicd.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request,'myapp/detail.html',{
#             'question':question,
#             'error_message':'you did not select a choice...'
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button
#         return HttpResponseRedirect(reverse('results',args = (question.id,)))
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

def vote(request,question_id):
    question = get_object_or_404(Question,pk = question_id)
    try:
        selected_choice = question.choicd_set.get(pk=request.POST['choice'])
    except(KeyError,Choicd.DoesNotExist):
        # Redisplay the question voting form.
        return render(request,'myapp/detail.html',{
            'question':question,
            'error_message':"you didn't select a choice..."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('results',args=(question.id,)))


