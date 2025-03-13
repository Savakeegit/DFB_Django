from django.urls import include, path
from api.spectacular.urls import urlpatterns as documentation_urls
from users.urls import urlpatterns as users_urls
from dogs.urls import urlpatterns as dogs_urls

app_name = 'api'

urlpatterns = [
    path('auth/', include('djoser.urls.jwt')),
]
urlpatterns += documentation_urls
urlpatterns += users_urls
urlpatterns += dogs_urls