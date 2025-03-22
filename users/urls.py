from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import users

router = DefaultRouter()


router.register(r'registration', users.RegistrationView, 'user-registration')

urlpatterns = [
    path('users/check/', users.CheckUserView.as_view(), name='user-tg-check'),
]

urlpatterns += path('users/', include(router.urls)),

