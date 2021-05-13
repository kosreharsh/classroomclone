from django.urls import path
from .views import *
app_name = 'quiz'

urlpatterns = [
    path('<str:quizname>/', quiz_question, name='quiz_test'),
    # path(/create_quiz/,,name='create_quiz'),
    path('api/<str:quizname>/', api_for_quiz, name='quiz_test_api'),
    path('api/<str:quizname>/marks/', api_for_quiz_mark, name='quiz_test_mark')
]
