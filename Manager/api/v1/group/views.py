from rest_framework import viewsets, decorators, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import GroupSerializer, GroupMemberSerializer
from api.v1.post.serializers import PostSerializer
from api.v1.quiz.serializers import QuizTestSerializer
from api.v1.assignment.serializers import AssignmentSerializer, AssignmentFilesSerializer

from api.v1.permissions import UserPermission, CreatorPermission

from group.models import Group, GroupMember
from django.db.models import Q


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def get_queryset(self):
        queryset = Group.objects.filter(
            Q(members=self.request.user) | Q(creator=self.request.user)).distinct()
        return queryset

    @action(detail=True, methods=['post'])
    @decorators.permission_classes([UserPermission])
    def addposts(self, request, pk=None):
        data = request.data
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            group = self.get_object()
            user = self.request.user
            serializer.save(user=user, group=group)
            return Response({"msg": "post is added"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"msg": "data is not valid"}, status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    @decorators.permission_classes([CreatorPermission])
    def createQuiz(self, request, pk=None):
        data = request.data
        serializer = QuizTestSerializer(data=data)
        if serializer.is_valid():
            group = self.get_object()
            serializer.save(group=group)
            return Response({"msg": "Quiz is created"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"msg": "data is not valid"}, status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    @decorators.permission_classes([CreatorPermission])
    def add_assignment(self, request, pk=None):
        data = request.data
        serializer = AssignmentSerializer(data=data)
        if serializer.is_valid():
            group = self.get_object()
            serializer.save(group=group)
            return Response({"msg": "Assignment is created"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"msg": "data is not valid"}, status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    @decorators.permission_classes([CreatorPermission])
    def add_assignmentfiles(self, request, pk=None):
        data = request.data
        serializer = AssignmentFilesSerializer(data=data)
        if serializer.is_valid():
            group = self.get_object()
            serializer.save(group=group)
            return Response({"msg": "Assignment Files is added"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"msg": "data is not valid"}, status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class GroupMemberViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = GroupMember.objects.all()
    serializer_class = GroupMemberSerializer
