from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth import get_user_model

User = get_user_model()


class Habit(models.Model):
    """
    Модель привычки.

    Атрибуты:
        user (ForeignKey): Пользователь, создатель привычки.
        location (str): Место, где необходимо выполнять привычку.
        time (str): Время, когда необходимо выполнять привычку.
        action (str): Действие, представляющее привычку.
        pleasant_habit (bool): Признак приятной привычки.
        related_habit (ForeignKey): Связанная привычка (если есть).
        frequency (int): Периодичность выполнения привычки в днях (по умолчанию - 1).
        reward (str): Вознаграждение за выполнение привычки.
        time_to_complete (int): Время, необходимое для выполнения привычки в секундах.
        is_public (bool): Признак публичности привычки.
        last_performed (DateTimeField): Дата последнего выполнения привычки.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    time = models.TimeField()
    action = models.CharField(max_length=255)
    pleasant_habit = models.BooleanField(default=False)
    related_habit = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    frequency = models.PositiveIntegerField(default=1)
    reward = models.CharField(max_length=255, blank=True, null=True)
    time_to_complete = models.PositiveIntegerField()
    is_public = models.BooleanField(default=False)
    last_performed = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "Habit"
        verbose_name_plural = "Habits"
        unique_together = ('user', 'action')

    def clean(self):
        """
        Валидирует экземпляр привычки перед сохранением.

        Проверяет, соответствуют ли значения полей модели заданным условиям.
        В случае нарушения правил валидации выбрасывает исключение ValidationError.

        Исключения:
            ValidationError: Если любое из правил валидации нарушено.
            - Если привычка отмечена как приятная, она не может иметь вознаграждение или связанную привычку.
            - Время выполнения не должно превышать 120 секунд.
            - Привычки для связанных привычек должны быть приятными.
            - Нельзя одновременно указывать вознаграждение и связанную привычку.
            - Периодичность выполнения должна быть от 1 до 7 дней.
            - Привычка должна выполняться хотя бы один раз в неделю.
        """

        if self.reward and self.related_habit:
            raise ValidationError("You cannot specify both a reward and a related habit.")

        if self.is_pleasant_habit:
            if self.reward or self.related_habit:
                raise ValidationError("Pleasant habits cannot have a reward or related habit.")

        if self.time_to_complete > 120:
            raise ValidationError("Execution time must not exceed 120 seconds.")

        if self.related_habit and not self.related_habit.is_pleasant_habit:
            raise ValidationError("Related habit must be a pleasant habit.")

        if self.frequency < 1 or self.frequency > 7:
            raise ValidationError("Frequency must be between 1 and 7 days.")

        if self.last_performed and self.last_performed < timezone.now() - timedelta(weeks=1):
            raise ValidationError("You must perform the habit at least once a week.")
