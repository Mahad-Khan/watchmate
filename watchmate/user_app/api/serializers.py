from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework import status



class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True }
        }

    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        email = self.validated_data['email']

        if not email:            
            raise serializers.ValidationError({"error": "email may not be blank"})

        if User.objects.filter(email=email).exists():
            res = serializers.ValidationError({"error": "Email already exists"})
            res.status_code = 409
            raise res 

        if password != password2:
            res = serializers.ValidationError({"error": "Those passwords didn't match. Try again."})
            res.status_code = 401
            raise res

        user = User(username=self.validated_data['username'], email=email)
        user.set_password(password)
        user.save()
        return user
        