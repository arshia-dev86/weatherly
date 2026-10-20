from rest_framework import serializers

class WeatherApicurrentSerializer(serializers.Serializer):
    datetime = serializers.CharField()
    temp = serializers.FloatField()
    humidity = serializers.FloatField()
    feelslike = serializers.FloatField()
    icon = serializers.CharField()
    
class WeatherApiDaysSerializer(serializers.Serializer):
    datetime = serializers.CharField()
    tempmax = serializers.FloatField()
    tempmin = serializers.FloatField()
    feelslikemax = serializers.FloatField()
    feelslikemin = serializers.FloatField()
    humidity = serializers.FloatField()
    description = serializers.CharField()
    icon = serializers.CharField()

class WeatherApiMainSerializer(serializers.Serializer):
    address = serializers.CharField()
    timezone = serializers.CharField()
    description = serializers.CharField()
    currentConditions = WeatherApicurrentSerializer()
    days = WeatherApiDaysSerializer(many=True)





