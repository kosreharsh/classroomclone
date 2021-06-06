from django.db import models

# Create your models here.


class TodoTasks(models.Model):
    title = models.CharField(max_length=200)
    deadline = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    task_done = models.BooleanField(default=False)

    def __str__(self):
        return self.title
