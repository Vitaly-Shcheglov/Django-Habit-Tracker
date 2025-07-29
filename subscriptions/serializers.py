from rest_framework import serializers
from .models import Subscription

class SubscriptionSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Subscription.
    Позволяет преобразовывать данные подписок в JSON-формат и обратно.
    """
    class Meta:
        model = Subscription
        fields = ['id', 'user', 'habit', 'created_at']
        read_only_fields = ['user', 'created_at']
