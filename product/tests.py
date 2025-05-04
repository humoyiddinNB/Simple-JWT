from http.client import responses

from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

from product.models import Category


class ProductTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='user', password='user')
        self.category = Category.objects.create(name='Phones')

        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)

        self.product_data = {
            'category': self.category.id,
            'name': "Iphone 12",
            'desc': "Ajoyib",
            "price": 1000
        }

        self.create_product_url = reverse('create')
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)

        response = self.client.post(self.create_product_url, data=self.product_data)
        self.product_id = response.data['data']['id']

        self.update_product_url = reverse('update', args=[self.product_id])
        self.detail_product_url = reverse('detail', args=[self.product_id])
        self.delete_product_url = reverse('delete', args=[self.product_id])
        self.list_product_url = reverse('list')


    def test_product_create(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        response = self.client.post(self.create_product_url, data=self.product_data)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['data']['name'], "Iphone 12")


    def test_update_product(self):

        update_data = {
        'name': 'Iphone 13',
        'desc': 'Yangi model',
        'price': 1200,
        'category': self.category.id
        }

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        response = self.client.put(self.update_product_url, update_data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['data']['name'], 'Iphone 13')
        self.assertEqual(response.data['data']['price'], 1200)


    def test_delete_product(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)

        response = self.client.post(self.delete_product_url)
        self.assertEqual(response.status_code, 204)














