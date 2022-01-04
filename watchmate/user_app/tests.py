from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token


class RegisterTestCase(APITestCase):

    def test_register(self):
        data ={
            "username": "example",
            "email":"example@gmail.com",
            "password": "password",
            "password2": "password"
            }
        response = self.client.post(reverse('register'), data, format='json')
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)


class LoginLogoutTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='example101', password='Pass@123')

    def test_login(self):
        """ test that login successful return status code """
        data ={
            "username": "example101",
            "password": "Pass@123"
        }
        response = self.client.post(reverse('login'), data, format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_logout(self):
        """ test that logout successful and return status code """
        self.token = Token.objects.get(user__username='example101')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key) # carrying a token
        response = self.client.post(reverse('logout'))
        self.assertEqual(response.status_code,status.HTTP_200_OK)

