from rest_framework import viewsets, decorators, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from group.serializers import GroupSerializer, GroupMemberSerializer
from group.models import Group, GroupMember
from django.db.models import Q
from post.serializer import PostSerializer
from post.models import Post


class UserPermission(permissions.BasePermission):
    message = 'User not allowed.'

    def has_object_permission(self, request, view, obj):
        user = request.user
        queryset = GroupMember.objects.filter(group=obj)
        for object in queryset:
            if user == object.user:
                return True
        return False


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
        # if post.is_valid():
        #     post.save()
        #     return Response({"msg": "post is added"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"msg": "data is not valid"}, status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class GroupMemberViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = GroupMember.objects.all()
    serializer_class = GroupMemberSerializer
