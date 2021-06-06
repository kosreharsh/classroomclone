from __future__ import absolute_import
from celery import shared_task
from celery.decorators import task
from .models import Assignment
from post.models import Post
from group.models import Group
from django.contrib.auth import get_user_model

User = get_user_model()


@shared_task
def test(param):
    return 'The tasks executed with the following parameter: "%s" '


@task(name="add_task_in_post")
def add_task_in_post(username, assignment_id, group_id):
    group = Group.objects.get(id=group_id)
    assignment = Assignment.objects.get(id=assignment_id)
    user = User.objects.filter(username=username).first()
    post = Post.objects.create(user=user, group=group)
    post.message = assignment.title
    post.save()
    print(post.message)
