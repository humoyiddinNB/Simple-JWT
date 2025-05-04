from http.client import responses

from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse


class AuthTest(APITestCase):
    def setUp(self):
        self.login_url = reverse('login')
        self.regis_url = reverse('register')
        self.logout_url = reverse('logout')
        self.test_url = reverse('test')

        self.user_data = {
            'username' : "user",
            'password' : "user"
        }


        self.client.post(self.regis_url, self.user_data)
        response = self.client.post(self.login_url, self.user_data)

        self.refresh_token = response.data['refresh']
        self.access_token = response.data['access']


    def test_regis(self):
        data = {
            'username' : 'user1',
            'password' : 'user1'
        }

        response = self.client.post(self.regis_url, data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['data'], 'user1')
        self.assertEqual(response.data['msg'], "ro'yxatdan o'tdingiz")


    def test_login(self):
        response = self.client.post(self.login_url, self.user_data)


        self.assertEqual(response.status_code, 200)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)


    def test_logout(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        response = self.client.post(self.logout_url, {"refresh" : self.refresh_token})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['msg'], 'Hayir, salomat boling')



    def test_nimadir_not(self):
        response = self.client.get(self.test_url)

        self.assertEqual(response.status_code, 401)
        self.assertNotIn('msg', response.data)

    def test_nimadir(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)

        response = self.client.get(self.test_url)

        self.assertEqual(response.status_code, 200)
        self.assertIn('msg', response.data)
        self.assertEqual(response.data['msg'], "Nimadir")