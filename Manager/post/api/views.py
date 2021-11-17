from rest_framework import viewsets, permissions, status, decorators
from post.serializer import PostSerializer, CommentSerializer
from post.models import Comment, Post
from group.models import GroupMember, Group
from rest_framework.decorators import action
from rest_framework.response import Response


class UserPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user
        queryset = GroupMember.objects.filter(group=obj.group)
        for object in queryset:
            if user == object.user:
                return True
        return False


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_class = UserPermission

    @action(detail=True, methods=['post'])
    @decorators.permission_classes([UserPermission])
    def addcomments(self, request):
        data = request.data
        comment = CommentSerializer(data=data)
        obj = self.get_object()
        comment.post = obj
        comment.user = self.request.user
        comment.save()
        return Response({"msg": "comment is added"}, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['delete'])
    def deletecomment(self, request):
        id = request.data.get('id')
        try:
            comment = Comment.objects.get(id=id)
            comment.delete()
            return Response({'msg': 'Comment deleted'}, status=status.HTTP_200_OK)
        except Comment.DoesNotExist:
            return Response({'msg': 'Comment does not exist'}, status=status.HTTP_404_NOT_FOUND)
