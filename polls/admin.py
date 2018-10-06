from django.contrib import admin
from .models import Question, Choice


class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Your name', {'fields': ['publisher_name']}),
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['publish_date']}),
    ]
    list_display = ('publisher_name', 'question_text', 'publish_date')
    list_filter = ["publish_date"]
    list_per_page = 10
    inlines = [ChoiceInLine]


admin.site.register(Question, QuestionAdmin)
