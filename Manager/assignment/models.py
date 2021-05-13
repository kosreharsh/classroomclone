from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model  
from group.models import Group
from django.utils.text import slugify
user = get_user_model()

# Create your models here.
class Assignment(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(blank=True,null=True)
    task = models.CharField(max_length=250,blank=True,null=True)
    task_created = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField(blank=True,null=True)
    attachments = models.FileField(blank=True,null=True)
    group = models.ForeignKey(Group,on_delete = models.CASCADE)

    def __str__(self):
        return self.group.name + " " + self.id

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)

class Response(models.Model):
    responses = models.FileField(blank=True,null=True)
    submitted_at = models.DateTimeField(auto_now=True)
    student = models.ForeignKey(user ,on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment,on_delete=models.CASCADE)
    