from .models import Question, Choice
from django.shortcuts import render, get_object_or_404
from django.http import Http404


def index(request):
    latest_five = Question.objects.order_by("-publish_date")[:5]
    context = {
        'latest_five': latest_five,
    }
    return render(request, "polls/index.html", context)


def details(request, question_id):
    q = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/details.html', {"question": q})


def results(request, question_id):
    return


def votes(request, question_id):
    return
