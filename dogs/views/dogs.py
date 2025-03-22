from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import AllowAny

from common.permissions import IsSafeSender
from common.views.mixins import LRCUDViewSet
from dogs.models.dogs import Dog
import dogs.serializers.dogs as dogs_serializers
from dogs.permissions import IsMyDog


@extend_schema_view(
    list=extend_schema(summary='Список собак', tags=['Собаки']),
    retrieve=extend_schema(summary='Деталка собаки', tags=['Собаки']),
    create=extend_schema(summary='Добавить собаку', tags=['Собаки']),
    partial_update=extend_schema(summary='Изменить собаку частично', tags=['Собаки']),
    destroy=extend_schema(summary='Убрать собаку', tags=['Собаки']),
)
class DogsView(LRCUDViewSet):
    http_method_names = ('get', 'post', 'patch', 'delete')
    # permission_classes = [IsMyDog, IsSafeSender]
    serializer_class = dogs_serializers.DogListSerializer
    queryset = Dog.objects.all()
    filter_backends = (
        OrderingFilter,
        SearchFilter,
        DjangoFilterBackend,
    )
    ordering = ('name',)

    multi_serializer_class = {
        'list': dogs_serializers.DogListSerializer,
        'retrieve': dogs_serializers.DogRetrieveSerializer,
        'create': dogs_serializers.DogCreateSerializer,
        'partial_update': dogs_serializers.DogPartialUpdateSerializer,
        'destroy': dogs_serializers.DogDestroySerializer,
    }

    def get_queryset(self):
        print(self.request.user)
        qs = Dog.objects.select_related('owner').filter(owner=self.request.user)
        return qs