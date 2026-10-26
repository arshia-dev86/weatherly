from django.shortcuts import render
from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import WeatherApiMainSerializer
import requests
from django.conf import settings
# Create your views here.

weather_api_url = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/'
weather_api_key = settings.WEATHER_API_KEY

class WeatherApiView(APIView):
    def get(self,request):
        city = request.query_params.get('city')
        if not city : 
            return Response({
                'error': 'Please enter the city name'
            },
            status=400)
        
        city_lower = city.strip().lower()
        cache_key = f'city_{city_lower}'
        cached_data = cache.get(cache_key)
        
        if cached_data :
            return Response(data=cached_data)
        
        url = weather_api_url + f'{city_lower}/'
        params = {
            'key' : weather_api_key,
            'unitGroup': 'metric',
        }
        res = requests.get(url=url, params=params,timeout=10)
        if res.status_code == 200:
            data = res.json()
            serializer= WeatherApiMainSerializer(data=data)
            if serializer.is_valid():
                cache.set(cache_key,data, 30)
                return Response(data=serializer.validated_data)
        serializer = WeatherApiMainSerializer()
        return Response(serializer.errors)