from rest_framework import serializers
from watchlist_app.models import Movie

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    is_active = serializers.BooleanField()
    
    def create(self,validate_data):
        return Movie.objects.create(**validate_data)
    
    def update(self, instance, validate_data): # instance holds old values and validation_data new value
        instance.name = validate_data.get("name", instance.name)
        instance.description = validate_data.get("description", instance.description)
        instance.is_active = validate_data.get("is_active", instance.is_active)
        instance.save()
        return instance