from rest_framework import serializers, viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Habit


class HabitSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Habit.

    Позволяет преобразовывать экземпляры модели Habit в JSON-формат
    и обратно, а также проводить валидацию входящих данных.
    """

    class Meta:
        model = Habit
        fields = [
            "id",
            "user",
            "location",
            "time",
            "action",
            "pleasant_habit",
            "related_habit",
            "frequency",
            "reward",
            "time_to_complete",
            "is_public",
            "last_performed",
        ]


class HabitViewSet(viewsets.ModelViewSet):
    """
    Представление для работы с привычками.

    Обеспечивает полный набор операций CRUD (создание, чтение, обновление, удаление)
    для модели Habit. Доступ к данным ограничен только для аутентифицированных пользователей.
    """

    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Возвращает набор данных привычек для текущего пользователя.

        Фильтрует привычки по текущему пользователю, чтобы каждый пользователь
        видел только свои привычки.

        Returns:
            QuerySet: Набор привычек, относящихся к текущему пользователю.
        """
        user = self.request.user
        return Habit.objects.filter(user=user)

    def perform_create(self, serializer):
        """
        Сохраняет новый экземпляр привычки, связанный с текущим пользователем.

        Параметры:
            serializer (HabitSerializer): Сериализатор, содержащий данные для создания привычки.
        """
        serializer.save(user=self.request.user)
