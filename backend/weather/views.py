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
        city = request.query_params['city']
        url = weather_api_url + f'{city}/'
        params = {
            'key' : weather_api_token
        }
        res = requests.get(url=url, params=params)
        if res.status_code == 200:
            data = res.json()
            serializer= WeatherApiMainSerializer(data=data)
            if serializer.is_valid():
                return Response(data=serializer.validated_data)    
        return Response(serializer.errors)