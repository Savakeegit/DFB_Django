from rest_framework.permissions import IsAuthenticated


class IsMyDog(IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        else:
            return False