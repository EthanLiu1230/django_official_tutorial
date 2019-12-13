from django.test import TestCase

import datetime
from django.utils import timezone

from .models import Question
from django.urls import reverse


# Create your tests here.
class TestQuestion(TestCase):
    def test_was_published_recently_with_future_question(self):
        future_time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=future_time)
        self.assertIs(future_question.was_published_recently(), False)


def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            []
        )

    def test_two_past_questions(self):
        create_question("Past question 1.", -30)
        create_question('Past question 2.', -5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past 2.>', '<Question: Past question 1.>']
        )
