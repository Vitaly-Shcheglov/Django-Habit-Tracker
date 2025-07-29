from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Subscription
from .serializers import SubscriptionSerializer

class SubscriptionViewSet(viewsets.ModelViewSet):
    """
    Представление для работы с подписками на привычки.
    """
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Возвращает подписки для текущего пользователя."""
        user = self.request.user
        return Subscription.objects.filter(user=user)
    