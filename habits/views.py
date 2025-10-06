from rest_framework import generics, viewsets
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


class UserHabitListView(generics.ListAPIView):
    """
    Представление для получения списка привычек текущего пользователя с пагинацией.
    """

    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class PublicHabitListView(generics.ListAPIView):
    """
    Представление для получения списка публичных привычек.
    """

    serializer_class = HabitSerializer

    def get_queryset(self):
        return Habit.objects.filter(is_public=True)


class HabitCreateView(generics.CreateAPIView):
    """
    Представление для создания новой привычки.
    """

    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class HabitUpdateView(generics.UpdateAPIView):
    """
    Представление для редактирования привычки.
    """

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]


class HabitDeleteView(generics.DestroyAPIView):
    """
    Представление для удаления привычки.
    """

    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated]
