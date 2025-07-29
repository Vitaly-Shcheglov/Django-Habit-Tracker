from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели User.
    Позволяет преобразовывать данные пользователей в JSON-формат и обратно.
    """
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """Создает нового пользователя с зашифрованным паролем."""
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    