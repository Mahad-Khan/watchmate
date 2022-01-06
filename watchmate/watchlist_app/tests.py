from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from watchlist_app import models

# Create your tests here.
class StreamPlatformTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username='mahad',
            email='abc@xyz.com',
            password='pass123')
        # self.user = User.objects.create(username='foobar', password='Pass@123')
        # self.user.is_staff = True
        self.token = Token.objects.get(user__username='mahad')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.stream = models.StreamPlatform.objects.create(name="Amazon",
                                            about="Lumber two Streaming Platform",
                                            website="https://www.amazon.com/")

    def test_streamplatform_create(self):
        "test that only admin can create platform and return status"
        data ={
            "name":"Netflix",
            "about":"Lumber one Streaming Platform",
            "website":"https://www.netflix.com/"
        }
        response = self.client.post(reverse('streamplatform-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_streamplatform_list(self):
        """ test that return platform list """
        response = self.client.get(reverse('streamplatform-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_streamplatform_ind(self):
        """ test that return specific platform  """
        response = self.client.get(reverse('streamplatform-detail', args=(self.stream.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_streamplatform_update(self):
        """test that update platform"""
        data ={
            "name":"Amazon",
            "about":"Lumber 2 Streaming Platform",
            "website":"https://www.Amazon.com/"
        }
        response = self.client.put(reverse('streamplatform-detail', args=(self.stream.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_streamplatform_update(self):
        """test that update  platform"""
        data ={
            "name":"Amazon",
            "about":"Lumber 2 Streaming Platform",
            "website":"https://www.Amazon.com/"
        }
        response = self.client.put(reverse('streamplatform-detail', args=(self.stream.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_streamplatform_delete(self):
        """test that delete platform"""
        response = self.client.delete(reverse('streamplatform-detail', args=(self.stream.id,)))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)