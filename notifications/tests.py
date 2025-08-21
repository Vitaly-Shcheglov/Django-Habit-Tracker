from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from .models import Notification
from .serializers import NotificationSerializer
from users.models import CustomUser


class NotificationModelTest(TestCase):
    """
    Тесты для модели Notification.
    """

    def setUp(self):
        """
        Создает пользователя и уведомление для тестирования.
        """
        self.user = CustomUser.objects.create(
            email="testuser@example.com", password="testpassword", phone="1234567890", city="Test City"
        )
        self.notification = Notification.objects.create(
            user=self.user,
            message="Your habit is due!",
        )

    def test_notification_creation(self):
        """
        Проверяет, что уведомление было создано правильно.
        """
        self.assertEqual(self.notification.user, self.user)
        self.assertEqual(self.notification.message, "Your habit is due!")

    def test_notification_str(self):
        """
        Проверяет строковое представление уведомления.
        """
        self.assertEqual(str(self.notification), f"Notification for {self.user.username}: Your habit is due!")


class NotificationAPITest(TestCase):
    """
    Тесты для API представлений уведомлений.
    """

    def setUp(self):
        """
        Создает клиента и пользователя для тестирования API.
        """
        self.client = APIClient()
        self.user = CustomUser.objects.create(
            email="testuser@example.com", password="testpassword", phone="1234567890", city="Test City"
        )
        self.client.force_authenticate(user=self.user)

    def test_create_notification(self):
        """
        Проверяет, что пользователь может создать новое уведомление.
        """
        response = self.client.post(
            "/api/notifications/",
            {
                "message": "Your habit is due!",
            },
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Notification.objects.count(), 1)
        self.assertEqual(Notification.objects.get().message, "Your habit is due!")

    def test_get_user_notifications(self):
        """
        Проверяет, что пользователь может получить свой список уведомлений.
        """
        self.client.post(
            "/api/notifications/",
            {
                "message": "Your habit is due!",
            },
        )
        response = self.client.get("/api/notifications/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class NotificationSerializerTest(TestCase):
    """
    Тесты для сериализатора NotificationSerializer.
    """

    def test_notification_serializer_valid(self):
        """
        Проверяет, что валидные данные сериализуются правильно.
        """
        user = CustomUser.objects.create(
            email="testuser@example.com", password="testpassword", phone="1234567890", city="Test City"
        )
        notification_data = {
            "user": user.id,
            "message": "Your habit is due!",
        }
        serializer = NotificationSerializer(data=notification_data)
        self.assertTrue(serializer.is_valid())

    def test_notification_serializer_invalid(self):
        """
        Проверяет, что невалидные данные не проходят валидацию.
        """
        notification_data = {}
        serializer = NotificationSerializer(data=notification_data)
        self.assertFalse(serializer.is_valid())
