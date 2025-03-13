from django.contrib.auth import get_user_model
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_200_OK, HTTP_204_NO_CONTENT
from rest_framework.views import APIView
from yaml import serialize

from config import settings
from common.views.mixins import CViewSet
from users.serializers.api import users as user_serializer
from rest_framework.response import Response


User = get_user_model()


@extend_schema_view(
    create=extend_schema(summary='Регистрация пользователя', tags=['Аутентификация & Авторизация']),
)
class RegistrationView(CViewSet):
    queryset = User.objects.all()
    http_method_names = ('post', )
    permission_classes = [AllowAny]
    serializer_class = user_serializer.RegistrationSerializer


@extend_schema_view(
    post=extend_schema(summary='Проверка на наличие пользователя', tags=['Аутентификация & Авторизация']),
)
class CheckUserView(APIView):

    serializer_class = user_serializer.CheckUserSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        if User.objects.filter(telegram_id=request.data['telegram_id']):
            return Response(status=HTTP_200_OK)
        else:
            return Response(status=HTTP_204_NO_CONTENT)


@extend_schema_view(
    post=extend_schema(summary='Получение refresh токена из БД', tags=['Аутентификация & Авторизация']),
)
class GetRefreshTokenFromInstanceView(APIView):

    serializer_class = user_serializer.RefreshTokenForUserSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        bot_secret_key = request.headers.get('X-Bot-Secret-Key')
        #f bot_secret_key != settings.BOT_SECRET_KEY:
            #raise AuthenticationFailed("Invalid bot secret key")
        #получаем пользователя
        user = User.objects.get(telegram_id=request.data['telegram_id'])
        #получаем его рефреш
        refresh = user.refresh_token
        #возвращаем
        return Response({
            'refresh_token': str(refresh),
        })


@extend_schema_view(
    post=extend_schema(
        request=user_serializer.EditRefreshTokenForUserSerializer,
        summary='Изменение refresh токена в БД', tags=['Аутентификация & Авторизация']),
)
class EditRefreshTokenForUserView(APIView):

    permission_classes = [AllowAny]

    def post(self, request):
        bot_secret_key = request.headers.get('X-Bot-Secret-Key')
        if bot_secret_key != settings.BOT_SECRET_KEY:
            raise AuthenticationFailed("Invalid bot secret key")

        user = User.objects.get(telegram_id=request.data['telegram_id'])

        serializer = user_serializer.EditRefreshTokenForUserSerializer(
            instance=user, data=request.data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=HTTP_204_NO_CONTENT)