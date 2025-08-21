from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from habits.models import Habit

from .models import Subscription
from .serializers import SubscriptionSerializer
from users.models import CustomUser


class SubscriptionModelTest(TestCase):
    """
    Тесты для модели Subscription.
    """

    def setUp(self):
        """
        Создает пользователя и привычку для тестирования.
        """
        self.user = CustomUser.objects.create(
            email="testuser@example.com", password="testpassword", phone="1234567890", city="Test City"
        )
        self.habit = Habit.objects.create(
            user=self.user,
            location="Park",
            time="10:00:00",
            action="Jogging",
            pleasant_habit=False,
            frequency=1,
            time_to_complete=60,
            is_public=True,
        )
        self.subscription = Subscription.objects.create(
            user=self.user,
            habit=self.habit,
        )

    def test_subscription_creation(self):
        """
        Проверяет, что подписка была создана правильно.
        """
        self.assertEqual(self.subscription.user, self.user)
        self.assertEqual(self.subscription.habit, self.habit)

    def test_subscription_str(self):
        """
        Проверяет строковое представление подписки.
        """
        self.assertEqual(str(self.subscription), f"Subscription for {self.user.username} to habit {self.habit.action}")


class SubscriptionAPITest(TestCase):
    """
    Тесты для API представлений подписок.
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

        self.habit = Habit.objects.create(
            user=self.user,
            location="Park",
            time="10:00:00",
            action="Jogging",
            pleasant_habit=False,
            frequency=1,
            time_to_complete=60,
            is_public=True,
        )

    def test_create_subscription(self):
        """
        Проверяет, что пользователь может создать новую подписку.
        """
        response = self.client.post(
            "/api/subscriptions/",
            {
                "habit": self.habit.id,
            },
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Subscription.objects.count(), 1)
        self.assertEqual(Subscription.objects.get().habit, self.habit)

    def test_get_user_subscriptions(self):
        """
        Проверяет, что пользователь может получить свой список подписок.
        """
        self.client.post(
            "/api/subscriptions/",
            {
                "habit": self.habit.id,
            },
        )
        response = self.client.get("/api/subscriptions/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class SubscriptionSerializerTest(TestCase):
    """
    Тесты для сериализатора SubscriptionSerializer.
    """

    def test_subscription_serializer_valid(self):
        """
        Проверяет, что валидные данные сериализуются правильно.
        """
        user = CustomUser.objects.create(
            email="testuser@example.com", password="testpassword", phone="1234567890", city="Test City"
        )
        habit = Habit.objects.create(
            user=user,
            location="Park",
            time="10:00:00",
            action="Jogging",
            pleasant_habit=False,
            frequency=1,
            time_to_complete=60,
            is_public=True,
        )
        subscription_data = {
            "user": user.id,
            "habit": habit.id,
        }
        serializer = SubscriptionSerializer(data=subscription_data)
        self.assertTrue(serializer.is_valid())

    def test_subscription_serializer_invalid(self):
        """
        Проверяет, что невалидные данные не проходят валидацию.
        """
        subscription_data = {}
        serializer = SubscriptionSerializer(data=subscription_data)
        self.assertFalse(serializer.is_valid())
