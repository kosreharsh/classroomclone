from rest_framework import viewsets, status, decorators, action

from .serializers import (AssignmentSerializer, AssignmentFilesSerializer,
                          ResponseSerializer, ResponseFilesSerializer)
from assignment.models import Assignment, Response, AssignmentFiles, ResponseFiles
from api.v1.permissions import CreatorPermission, UserPermission


class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer


class AssignmentFilesViewSet(viewsets.ModelViewSet):
    queryset = AssignmentFiles.objects.all()
    serializer_class = AssignmentFilesSerializer


class ResponseViewSet(viewsets.ModelViewSet):
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer


class ResponseFilesViewSet(viewsets.ModelViewSet):
    queryset = ResponseFiles.objects.all()
    serializer_class = ResponseFilesSerializer
