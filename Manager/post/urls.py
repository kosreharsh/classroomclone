from django.urls import path
from . import views
app_name = 'post'

urlpatterns = [
    path('', views.PostList.as_view(), name="post_all"),
    path('new/', views.CreatePost.as_view(), name="post_create"),
    path('<str:username>/<int:pk>/',views.PostDetail.as_view(),name="post_single"),
    path('delete/<int:pk>',views.DeletePost.as_view(),name="post_delete"),
  
]