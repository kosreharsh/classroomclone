from django.db import models
from django.db.models.fields import related
from django.utils import timezone
from django.contrib.auth import get_user_model
from group.models import Group
from django.utils.text import slugify
user = get_user_model()

# Create your models here.


def task_directory_path(instance, filename):
    return '{0}/{1}/{2}'.format(instance.assignment.group.slug, instance.assignment.title, filename)


def response_directory_path(instance, filename):
    return '{0}/Response/{1}'.format(instance.response.assignment.title, filename)


class Assignment(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, null=True)
    task = models.TextField(blank=True, null=True)
    task_created = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField(blank=True, null=True)
    group = models.ForeignKey(
        Group, related_name="group_assignment", on_delete=models.CASCADE)

    def __str__(self):
        return self.group.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class AssignmentFiles(models.Model):
    attachments = models.FileField(
        upload_to=task_directory_path, blank=True, null=True)
    assignment = models.ForeignKey(
        Assignment, related_name="assignment_file", on_delete=models.CASCADE)

    def __str__(self):
        return self.assignment.title


class Response(models.Model):

    submitted_at = models.DateTimeField(auto_now=True)
    student = models.ForeignKey(user, on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)

    def __str__(self):
        return self.student.username


class ResponseFiles(models.Model):
    rfiles = models.FileField(upload_to=response_directory_path, blank=True)
    response = models.ForeignKey(
        Response, related_name="response_file", on_delete=models.CASCADE)

    def __str__(self):
        return self.response.student.username
