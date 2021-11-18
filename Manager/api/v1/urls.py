from rest_framework import routers
from rest_framework.routers import DefaultRouter

from post.api.views import PostViewSet
from group.api.views import GroupViewSet, GroupMemberViewSet
from quiz.api.views import QuizTestViewSet

router = DefaultRouter()
router.register(r'post', PostViewSet)
router.register(r'group', GroupViewSet)
router.register(r'groupmembers', GroupMemberViewSet)
router.register(r'quiz', QuizTestViewSet)

urlpatterns = []
urlpatterns += router.urls
