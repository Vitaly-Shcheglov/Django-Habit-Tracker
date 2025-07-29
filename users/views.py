from django.contrib.auth import get_user_model
from rest_framework import generics
from .serializers import UserSerializer

User = get_user_model()

class UserListCreateView(generics.ListCreateAPIView):
    """
    Представление для создания и просмотра пользователей.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Представление для получения, обновления и удаления пользователя.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
