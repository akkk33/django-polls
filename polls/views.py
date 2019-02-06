from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Question, Choice


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_five"

    def get_queryset(self):
        return Question.objects.filter(publish_date__lte=timezone.now()).order_by("-publish_date")[:5]


class DetailsView(generic.DetailView):
    model = Question
    template_name = "polls/details.html"

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(publish_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    context_object_name = "q"
    template_name = "polls/results.html"


def votes(request, question_id):
    q = get_object_or_404(Question, pk=question_id)
    try:
        choice = q.choice_set.get(pk=request.POST['choice'])
    except (KeyError, choice.DoesNotExist):
        raise Http404("You didn't select a choice!")
    else:
        choice.votes += 1
        choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(q.id,)))
