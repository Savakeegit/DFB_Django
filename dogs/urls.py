from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from dogs.views import dogs

router = DefaultRouter()

router.register(r'', dogs.DogsView, 'organisations')

urlpatterns = [
    path('dogs/', include(router.urls)),
]
