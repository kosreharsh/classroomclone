from rest_framework import routers
from rest_framework.routers import DefaultRouter

from api.v1.post.views import PostViewSet
from api.v1.group.views import GroupViewSet, GroupMemberViewSet
from api.v1.quiz.views import QuizTestViewSet, UserQuizInfoViewSet, QuestionViewSet

router = DefaultRouter()
router.register(r'post', PostViewSet)
router.register(r'group', GroupViewSet)
router.register(r'groupmembers', GroupMemberViewSet)
router.register(r'quiz', QuizTestViewSet)
router.register(r'quiz_info', UserQuizInfoViewSet)
router.register(r'question', QuestionViewSet)


urlpatterns = []
urlpatterns += router.urls
