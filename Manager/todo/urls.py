from django.urls import path
from .views import TodoList, TaskRUD
from rest_framework.urlpatterns import format_suffix_patterns
app_name = 'todo'

urlpatterns = [

    ##path('celery/', celery_test, name='celery-test'),
    path('list-or-create/', TodoList.as_view(), name='todo-list'),
    path('rud/<int:pk>/', TaskRUD.as_view(), name='task-rud')

]

urlpatterns = format_suffix_patterns(urlpatterns)
