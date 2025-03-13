from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.exceptions import ParseError, NotFound
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class RegistrationSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'}, write_only=True
    )
    refresh_token = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = (
            'telegram_id',
            'username',
            'password',
            'refresh_token'
        )

    def validate_username(self, value):
        username = value
        if User.objects.filter(username=username).exists():
            raise ParseError(
                'Никнейм занят.'
            )
        return username

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        user = User.objects.create_user(
            telegram_id=validated_data.pop('telegram_id'),
            username=validated_data.pop('username'),
            password=validated_data.pop('password'),
        )
        refresh_token = RefreshToken.for_user(user)
        user.refresh_token = str(refresh_token)
        user.save()
        return user



class CheckUserSerializer(serializers.ModelSerializer):
    telegram_id = serializers.CharField(max_length=30)

    class Meta:
        model = User
        fields = (
            'telegram_id',
        )


class RefreshTokenForUserSerializer(serializers.ModelSerializer):
    telegram_id = serializers.CharField(max_length=30)

    class Meta:
        model = User
        fields = (
            'telegram_id',
        )


class EditRefreshTokenForUserSerializer(serializers.ModelSerializer):
    refresh_token = serializers.CharField()

    class Meta:
        model = User
        fields = (
            'refresh_token',
        )