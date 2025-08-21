from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from .models import Habit
from .serializers import HabitSerializer
from users.models import CustomUser

class HabitAPITests(APITestCase):
    """
    Тесты для API представлений привычек.
    """

    def setUp(self):
        """
        Создает клиента и пользователя для тестирования API.
        """
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(
            email="testuser@example.com", password="testpassword", phone="1234567890", city="Test City"
        )
        self.client.force_authenticate(user=self.user)

        self.habit_url = reverse("habits:create-habit")
        self.user_habit_url = reverse("habits:user-habits")
        self.public_habit_url = reverse("habits:public-habits")

    def test_create_habit(self):
        """Тест создания привычки."""
        data = {
            "location": "Park",
            "time": "10:00:00",
            "action": "Jogging",
            "pleasant_habit": False,
            "frequency": 1,
            "time_to_complete": 60,
            "is_public": True,
        }
        response = self.client.post(self.habit_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.count(), 1)
        self.assertEqual(Habit.objects.get().action, "Jogging")

    def test_user_habit_list(self):
        """Тест получения списка привычек текущего пользователя."""
        Habit.objects.create(
            user=self.user,
            location="Gym",
            time="08:00:00",
            action="Workout",
            pleasant_habit=False,
            frequency=1,
            time_to_complete=60,
            is_public=True,
        )
        response = self.client.get(self.user_habit_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_public_habit_list(self):
        """Тест получения списка публичных привычек."""
        Habit.objects.create(
            user=self.user,
            location="Park",
            time="10:00:00",
            action="Jogging",
            pleasant_habit=False,
            frequency=1,
            time_to_complete=60,
            is_public=True,
        )
        Habit.objects.create(
            user=self.user,
            location="Home",
            time="10:00:00",
            action="Reading",
            pleasant_habit=False,
            frequency=1,
            time_to_complete=60,
            is_public=False,
        )
        response = self.client.get(self.public_habit_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_habit(self):
        """Тест редактирования привычки."""
        habit = Habit.objects.create(
            user=self.user,
            location="Park",
            time="10:00:00",
            action="Jogging",
            pleasant_habit=False,
            frequency=1,
            time_to_complete=60,
            is_public=True,
        )
        url = reverse("habits:edit-habit", args=[habit.id])
        data = {"action": "Running"}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        habit.refresh_from_db()
        self.assertEqual(habit.action, "Running")

    def test_delete_habit(self):
        """Тест удаления привычки."""
        habit = Habit.objects.create(
            user=self.user,
            location="Park",
            time="10:00:00",
            action="Jogging",
            pleasant_habit=False,
            frequency=1,
            time_to_complete=60,
            is_public=True,
        )
        url = reverse("habits:delete-habit", args=[habit.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.count(), 0)


class HabitModelTest(TestCase):
    """
    Тесты для модели Habit.
    """

    def setUp(self):
        """
        Создает пользователя и привычку для тестирования.
        """
        self.user = CustomUser.objects.create_user(
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

    def test_habit_creation(self):
        """
        Проверяет, что привычка была создана правильно и принадлежит правильному пользователю.
        """
        self.assertEqual(self.habit.user, self.user)
        self.assertEqual(self.habit.location, "Park")
        self.assertEqual(self.habit.action, "Jogging")

    def test_habit_str(self):
        """
        Проверяет строковое представление привычки.
        """
        self.assertEqual(str(self.habit), f"Notification for {self.user.username}: Jogging")


class HabitSerializerTest(TestCase):
    """
    Тесты для сериализатора HabitSerializer.
    """

    def test_habit_serializer_valid(self):
        """
        Проверяет, что валидные данные сериализуются правильно.
        """
        habit_data = {
            "user": 1,
            "location": "Park",
            "time": "10:00:00",
            "action": "Jogging",
            "pleasant_habit": False,
            "frequency": 1,
            "time_to_complete": 60,
            "is_public": True,
        }
        serializer = HabitSerializer(data=habit_data)
        self.assertTrue(serializer.is_valid())

    def test_habit_serializer_invalid(self):
        """
        Проверяет, что невалидные данные не проходят валидацию.
        """
        habit_data = {
            "location": "Park",
            "time": "10:00:00",
            "action": "Jogging",
        }
        serializer = HabitSerializer(data=habit_data)
        self.assertFalse(serializer.is_valid())
