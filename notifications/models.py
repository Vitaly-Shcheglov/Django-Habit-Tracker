from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings


User = get_user_model()


class Notification(models.Model):
    """
    Модель уведомления, представляющая уведомления для пользователей.

    Атрибуты:
        user (ForeignKey): Пользователь, которому отправлено уведомление.
        message (str): Сообщение уведомления.
        created_at (DateTimeField): Время создания уведомления.
        is_read (bool): Признак, было ли уведомление прочитано пользователем.
    """

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Notification"
        verbose_name_plural = "Notifications"
        ordering = ["-created_at"]

    def __str__(self):
        """
        Возвращает строковое представление уведомления.

        Формат строки: "Notification for {username}: {message}".

        Возвращает:
            str: Строка, представляющая уведомление, которое включает
            имя пользователя и сообщение уведомления.
        """
        return f"Notification for {self.user.username}: {self.message}"
