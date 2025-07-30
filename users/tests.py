from django.test import TestCase
from .models import CustomUser
from rest_framework.test import APIClient
from rest_framework import status
from .serializers import UserSerializer

class CustomUserModelTest(TestCase):
    """
    Тесты для модели CustomUser.
    """

    def setUp(self):
        """
        Создает пользователя для тестирования.
        """
        self.user = CustomUser.objects.create_user(
            email='testuser@example.com',
            password='testpassword',
            phone='1234567890',
            city='Test City'
        )

    def test_user_creation(self):
        """
        Проверяет, что пользователь был создан правильно.
        """
        self.assertEqual(self.user.email, 'testuser@example.com')
        self.assertTrue(self.user.check_password('testpassword'))

    def test_user_str(self):
        """
        Проверяет строковое представление пользователя.
        """
        self.assertEqual(str(self.user), self.user.email)


class UserAPITest(TestCase):
    """
    Тесты для API представлений пользователей.
    """

    def setUp(self):
        """
        Создает клиента и пользователя для тестирования API.
        """
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(
            email='testuser@example.com',
            password='testpassword',
            phone='1234567890',
            city='Test City'
        )

    def test_create_user(self):
        """
        Проверяет, что можно создать нового пользователя.
        """
        response = self.client.post('/api/users/', {
            'email': 'newuser@example.com',
            'password': 'newpassword',
            'phone': '0987654321',
            'city': 'New City'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CustomUser.objects.count(), 2)

    def test_list_users(self):
        """
        Проверяет, что можно получить список пользователей.
        """
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class UserSerializerTest(TestCase):
    """
    Тесты для сериализатора UserSerializer.
    """

    def test_user_serializer_valid(self):
        """
        Проверяет, что валидные данные сериализуются правильно.
        """
        user_data = {
            'email': 'testuser@example.com',
            'password': 'testpassword',
            'phone': '1234567890',
            'city': 'Test City',
        }
        serializer = UserSerializer(data=user_data)
        self.assertTrue(serializer.is_valid())

    def test_user_serializer_invalid(self):
        """
        Проверяет, что невалидные данные не проходят валидацию.
        """
        user_data = {
        }
        serializer = UserSerializer(data=user_data)
        self.assertFalse(serializer.is_valid())
