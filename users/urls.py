from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import users

router = DefaultRouter()


router.register(r'registration', users.RegistrationView, 'user-registration')

urlpatterns = [
    path('users/check/', users.CheckUserView.as_view(), name='user-tg-check'),
    path('users/get-refresh-token/', users.GetRefreshTokenFromInstanceView.as_view(), name='get-refresh-token-from-instance'),
    path('users/edit-refresh-token/', users.EditRefreshTokenForUserView.as_view(), name='edit-refresh-token-for-user'),
]

urlpatterns += path('users/', include(router.urls)),

