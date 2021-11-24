from rest_framework import serializers
from watchlist_app.models import Movie


def check_name_len(value):
    if len(value) < 2:
        raise serializers.ValidationError("name is too short")


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(validators=[check_name_len])
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


    def validate_description(self, description):
        if len(description) < 2:
            raise serializers.ValidationError("description is too short")
        return description


    def validate(self, data):
        if data["name"] == data["description"]:
            raise serializers.ValidationError("Movie name and description should be different")


  


  
