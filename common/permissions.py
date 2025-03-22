from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied

User = get_user_model()

class IsTelegramUser(permissions.BasePermission):
    def has_permission(self, request, view):
        user = User.objects.filter(telegram_id=request.headers.get('X-Telegram-User-ID')).first()
        if user:
            request.user = user
            return True
        else:
            raise PermissionDenied('User not found')


class IsSafeSender(permissions.BasePermission):
    def has_permission(self, request, view):
        bot_secret_key = request.headers.get('X-Bot-Secret-Key')
        if bot_secret_key == settings.TELEGRAM_BOT_HEADER_SECRET_KEY:
            return True
        else:
            raise PermissionDenied("Request have't permission")
