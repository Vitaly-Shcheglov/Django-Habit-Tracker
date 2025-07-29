from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Habit
from .serializers import HabitSerializer

class HabitViewSet(viewsets.ModelViewSet):
    """
    Представление для работы с привычками.
    Обеспечивает полный набор операций CRUD для модели Habit.
    """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Возвращает набор привычек для текущего пользователя."""
        user = self.request.user
        return Habit.objects.filter(user=user)

    def perform_create(self, serializer):
        """Сохраняет новую привычку, связанную с текущим пользователем."""
        serializer.save(user=self.request.user)
