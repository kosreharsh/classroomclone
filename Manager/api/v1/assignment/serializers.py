from rest_framework import serializers
from assignment.models import Assignment, AssignmentFiles, Response, ResponseFiles
from django.contrib.auth import get_user_model
User = get_user_model()


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = '__all__'


class AssignmentFilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignmentFiles
        fields = '__all__'


class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Response
        fields = '__all__'


class ResponseFilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResponseFiles
        fields = '__all__'
