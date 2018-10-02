from django.http import HttpResponse
from .models import Question, Choice
from django.shortcuts import render


def index(request):
    latest_five = Question.objects.order_by("-publish_date")[:5]
    context = {
        'latest_five': latest_five,
    }
    return render(request, "polls/index.html", context)


def details(request, question_id):
    return HttpResponse("You're seeing question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def votes(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
