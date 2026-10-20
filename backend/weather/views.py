from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import WeatherApiMainSerializer
import requests
# Create your views here.

weather_api_url = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/'
weather_api_token = 'HF3N22WDDTG7YU5N5ECGS4WHH'

class WeatherApiView(APIView):
    def get(self,request):
        city = request.query_params.get('city')
        if not city : 
            return Response({
                'error': 'Please enter the city name'
            },
            status=400)
        url = weather_api_url + f'{city}/'
        params = {
            'key' : weather_api_token,
            'unitGroup': 'metric',
        }
        res = requests.get(url=url, params=params,timeout=10)
        if res.status_code == 200:
            data = res.json()
            serializer= WeatherApiMainSerializer(data=data)
            if serializer.is_valid():
                return Response(data=serializer.validated_data)
        serializer = WeatherApiMainSerializer()
        return Response(serializer.errors)