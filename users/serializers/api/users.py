from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.exceptions import ParseError, NotFound
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class RegistrationSerializer(serializers.ModelSerializer):
    username = serializers.CharField()

    class Meta:
        model = User
        fields = (
            'telegram_id',
            'username',
        )

    def validate_username(self, value):
        username = value
        if User.objects.filter(username=username).exists():
            raise ParseError(
                'Никнейм занят.'
            )
        return username

    def create(self, validated_data):
        user = User.objects.create_user(
            telegram_id=validated_data.pop('telegram_id'),
            username=validated_data.pop('username'),
        )

        user.save()
        return user



class CheckUserSerializer(serializers.ModelSerializer):
    telegram_id = serializers.CharField(max_length=30)

    class Meta:
        model = User
        fields = (
            'telegram_id',
        )