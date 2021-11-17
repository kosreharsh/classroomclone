"""Manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views
from post.api.views import PostViewSet
from group.api.views import GroupViewSet, GroupMemberViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'post', PostViewSet)
router.register(r'group', GroupViewSet)
router.register(r'groupmembers', GroupMemberViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('', views.index, name="landing-page"),
    path('', include("group.urls", namespace="group")),
    path('quiz/', include("quiz.urls", namespace="quiz")),
    path('task/', include("assignment.urls", namespace="assignment")),
    path('post/', include("post.urls", namespace="post")),
    path('todo/', include("todo.urls", namespace="todo")),
    path('account/', include("accounts.urls", namespace="accounts")),
    path('accounts/', include("django.contrib.auth.urls")),
    path('api-auth/', include('rest_framework.urls')),
]

if settings.DEBUG:

    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
