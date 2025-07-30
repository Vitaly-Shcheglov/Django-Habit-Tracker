from rest_framework import generics
from .models import Notification
from .serializers import NotificationSerializer


class NotificationListView(generics.ListCreateAPIView):
    """
    Представление для получения списка уведомлений и создания нового уведомления.
    """

    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer


class NotificationDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Представление для получения, обновления или удаления уведомления.
    """

    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
