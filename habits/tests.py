from .models import Habit
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient, APITestCase
from django.urls import reverse
from rest_framework import status

User = get_user_model()

class HabitAPITests(APITestCase):
    """
    Тесты для API представлений привычек.
    """

    def setUp(self):
        """
        Создает клиента и пользователя для тестирования API.
        """
        self.client = APIClient()
        self.user = User.objects.create_user(
            email="testuser@example.com", password="testpassword", phone="1234567890", city="Test City"
        )
        self.client.force_authenticate(user=self.user)

        self.habit_url = reverse("habits:create-habit")
        self.user_habit_url = reverse("habits:user-habits")
        self.public_habit_url = reverse("habits:public-habits")

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
