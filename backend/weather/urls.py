from django.urls import path
from .views import WeatherApiView

urlpatterns = [
    path('', WeatherApiView.as_view(),name="weather-api")
]
