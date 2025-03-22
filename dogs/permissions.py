from django.contrib.auth import get_user_model
from common.permissions import IsTelegramUser

User = get_user_model()

class IsMyDog(IsTelegramUser):
    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        else:
            return False

