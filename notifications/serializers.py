from rest_framework import serializers

from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Notification.

    Позволяет преобразовывать экземпляры модели Notification в JSON-формат
    и обратно, а также проводить валидацию входящих данных.
    """

    class Meta:
        model = Notification
        fields = ["id", "user", "message", "created_at", "is_read"]
        read_only_fields = ["created_at"]
