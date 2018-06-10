from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import  Question


def index(request) :
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

def detail(request,question_id):
    return HttpResponse('you are looking at question {}'.format(question_id))

def results(request,question_id):
    request = 'you are looking at the results of question %s'
    return HttpResponse(request % question_id)

def vote(request , question_id):
    return  HttpResponse('you are voting on question {}'.format(question_id))
