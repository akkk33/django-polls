from .models import Question, Choice
from django.shortcuts import render
from django.http import Http404


def index(request):
    latest_five = Question.objects.order_by("-publish_date")[:5]
    context = {
        'latest_five': latest_five,
    }
    return render(request, "polls/index.html", context)


def details(request, question_id):
    try:
        q = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("This question doesn't exist!")
    return render(request, 'polls/details.html', {"question": q})


def results(request, question_id):
    return


def votes(request, question_id):
    return
