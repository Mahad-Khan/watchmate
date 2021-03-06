from rest_framework import serializers
from watchlist_app.models import Watchlist, StreamPlatform, Review


class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Review
        exclude = ('watchlist',)         # saving in views--> serializer.save(watchlist=watch, review_user=review_user)
        # fields = ('__all__')


class WatchlistSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    # platform = serializers.CharField(source='platform.name')

    class Meta:
        model = Watchlist
        fields = "__all__"



class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchlistSerializer(many=True, read_only=True)                      # return whole object
    # watchlist = serializers.StringRelatedField(many=True, read_only=True)         # return thats implemented in __str__
    # watchlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True)     # return primary key
    # watchlist = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='watch-detail') # return objects' urls

    class Meta:
        model = StreamPlatform
        fields = ('__all__')

    def create(self, validated_data):
        if StreamPlatform.objects.filter(name=validated_data['name']).exists():
            res = serializers.ValidationError({"error": "platform name is already exist"})
            res.status_code = 409
            raise res
        else:
            return StreamPlatform.objects.create(**validated_data)









# ##########################  for practice  ##############################


# ################################# ModelSerializer class ############################################

# class MovieSerializer(serializers.ModelSerializer):
#     # custom field that does not exit in models or views
#     # read_only field
#     name_len = serializers.SerializerMethodField(method_name=None) 

#     class Meta:
#         model = Movie
#         fields = "__all__"
#         # fields = ["name", "description"]
#         # exclude = ["id"]
    
#     # method name should be get_[FieldName]
#     def get_name_len(self, object):
#         return len(object.name)


#     # field level validation
#     def validate_description(self, description):
#         if len(description) < 2:
#             raise serializers.ValidationError("description is too short")
#         return description

#     # field level validation
#     def validate_name(self, name):
#         if len(name) < 2:
#             raise serializers.ValidationError("description is too short")
#         return name

#     # object level validation
#     def validate(self, data):
#         if data["name"] == data["description"]:
#             raise serializers.ValidationError("Movie name and description should be different")
#         else:
#             return data


################################# Serializer class ############################################

# def check_name_len(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("name is too short")


# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[check_name_len])
#     description = serializers.CharField()
#     is_active = serializers.BooleanField()
    
#     def create(self,validate_data):
#         return Movie.objects.create(**validate_data)
    

#     def update(self, instance, validate_data): # instance holds old values and validation_data new value
#         instance.name = validate_data.get("name", instance.name)
#         instance.description = validate_data.get("description", instance.description)
#         instance.is_active = validate_data.get("is_active", instance.is_active)
#         instance.save()
#         return instance


#     def validate_description(self, description):
#         if len(description) < 2:
#             raise serializers.ValidationError("description is too short")
#         return description


#     def validate(self, data):
#         if data["name"] == data["description"]:
#             raise serializers.ValidationError("Movie name and description should be different")
