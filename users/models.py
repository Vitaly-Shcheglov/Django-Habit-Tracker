from django.contrib.auth.models import Group, Permission
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """
    Пользовательская модель пользователя, наследующая от AbstractUser.

    Включает дополнительные поля:
    - email: уникальный адрес электронной почты.
    - phone: номер телефона пользователя.
    - city: город проживания.
    - avatar: изображение профиля пользователя.

    Поля username и REQUIRED_FIELDS настроены для использования email в качестве имени пользователя.
    """

    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    city = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)
    telegram_chat_id = models.CharField(max_length=255, blank=True, null=True)

    username = None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["phone", "city"]

    groups = models.ManyToManyField(
        Group,
        related_name="customuser_groups",
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customuser_permissions",
        blank=True,
    )
