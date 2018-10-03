import datetime
from django.db import models
from django.utils import timezone


class Question(models.Model):
    publisher_name = models.CharField(max_length=60)
    question_text = models.CharField(max_length=140)
    publish_date = models.DateTimeField("Date published")

    def recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.publish_date <= now

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=256)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
