from rest_framework.decorators import api_view
from user_app.api.serializers import RegistrationSerializer
from rest_framework.response import Response
from rest_framework import status
from user_app import models
from rest_framework.authtoken.models import Token


@api_view(['POST'])
def registerations_view(request):
    
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "Registration Successful"
            data['username'] = account.username
            data['email'] = account.email
            data['token'] = Token.objects.get(user=account).key
        else:
            data = serializer.errors

        return Response(data)
