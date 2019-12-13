from django.contrib import admin

# Register your models here.
from .models import Question, Choice


# don't worry, Choice model already combined to Question in models.py
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Text', {'fields': ['question_text']}),
        ('Date Information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date', 'question_text']
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
