from django.contrib.auth.base_user import BaseUserManager
from rest_framework.exceptions import ParseError


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, telegram_id=None, username=None, password=None, refresh_token=None,  **extra_fields):
        user = self.model(**extra_fields)

        user.telegram_id = telegram_id
        user.username = username
        user.refresh_token = refresh_token

        if not password:
            user.password = None
        else:
            user.set_password(password)

        user.save(using=self._db)
        return user

    def create_user(self, telegram_id=None, username=None, password=None, refresh_token=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_active', True)

        return self._create_user(
            telegram_id, username, password, refresh_token, **extra_fields
        )

    def create_superuser(self, telegram_id=None, username=None,  password=None, refresh_token=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)

        return self._create_user(
            telegram_id, username, password, refresh_token, **extra_fields
        )