from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
from .models import *
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


@csrf_exempt
def api_for_quiz(request, quizname):
    try:
        quiz = QuizTest.objects.filter(quizname=quizname).first()
        questions = Question.objects.filter(quiz=quiz)
        questions_set = []
        for i in questions:
            question = {}
            question['question'] = i.question
            question['answer'] = i.answer
            options = []
            options.append(i.option1)
            options.append(i.option2)
            if len(i.option3) > 0:
                options.append(i.option3)
            if len(i.option4) > 0:
                options.append(i.option4)
            question['options'] = options
            questions_set.append(question)
        return JsonResponse(questions_set, safe=False)
    except QuizTest.DoesNotExist:
        return JsonResponse({'msg': 'quiz not found'})


@csrf_exempt
def api_for_quiz_mark(request, quizname):
    data = json.loads(request.body)
    print(data)
    return JsonResponse({'msg': 'successfully posted'})


def quiz_question(request, quizname):
    return render(request, 'quiz/quiz.html', {'quizname': quizname})
