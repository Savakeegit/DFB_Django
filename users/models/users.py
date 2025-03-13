from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from users.managers import CustomUserManager

class User(AbstractUser):
    telegram_id = models.CharField('Telegram ID', max_length=64, primary_key=True)
    username = models.CharField('Никнейм', max_length=36, unique=True, null=True, blank=True)
    email = models.EmailField('Почта', max_length=36, unique=True, null=True, blank=True, default=None,)
    refresh_token = models.CharField('Refresh Token', max_length=255, null=True, blank=True, default=None)

    objects = CustomUserManager()
    USERNAME_FIELD = 'telegram_id'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username