from django.contrib.auth.models import User
from rest_framework import serializers



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
            raise serializers.ValidationError({"error": "Email already exists"})
        
        if password != password2:
            raise serializers.ValidationError({"error": "Password and password2 are not equal"})

        user = User(username=self.validated_data['username'], email=email)
        user.set_password(password)
        user.save()
        return user
        