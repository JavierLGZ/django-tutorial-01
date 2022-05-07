from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question


def index(request):
    lastest_question_list = Question.objects.order_by('-pub_date')[:5]
    return render(request, "polls/index.html", {
        "lastest_question_list": lastest_question_list
    })


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {
        "question": question
    })


def results(request, question_id):
    return HttpResponse(f"You're looking at results of questions {question_id}")


def vote(request, question_id):
    return HttpResponse(f"You're voting at question {question_id}")
