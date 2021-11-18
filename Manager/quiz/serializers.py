from rest_framework import serializers
from .models import QuizTest, UserQuizInfo, Question
from group.serializers import GroupSerializer


class QuizTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizTest
        fields = '__all__'


class UserQuizInfoSerializer(serializers.ModelSerializer):
    quiz = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = UserQuizInfo
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        exclude = ('qimage',)
