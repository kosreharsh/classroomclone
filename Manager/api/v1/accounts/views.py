from django.contrib.auth.models import User
from rest_framework import viewsets, mixins
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
User = get_user_model()


class UserRegistrationViewSet(
        mixins.CreateModelMixin,
        mixins.RetrieveModelMixin,
        mixins.UpdateModelMixin,
        viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
