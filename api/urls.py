from django.urls import include, path

from api.spectacular.urls import urlpatterns as documentation_urls
app_name = 'api'

urlpatterns = [
    path('auth/', include('djoser.urls.jwt')),
]
urlpatterns += documentation_urls