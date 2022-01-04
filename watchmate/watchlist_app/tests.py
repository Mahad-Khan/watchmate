from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

# Create your tests here.
class StreamPlatformTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username='foobar',
            email='foo@bar.com',
            password='barbaz')
        # self.user = User.objects.create(username='foobar', password='Pass@123')
        # self.user.is_staff = True
        self.token = Token.objects.get(user__username='foobar')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_stream_platform_create(self):
        "test that only admin can create platform and return status"
        data ={
            "name":"Netflix",
            "about":"Lumber one Streaming Platform",
            "website":"https://www.netflix.com/"
        }
        response = self.client.post(reverse('streamplatform-list'), data, format='json')
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
