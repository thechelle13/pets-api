import json
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from petapi.models import Type

class TypeTests(APITestCase):

    fixtures = ['types']

    def setUp(self):
        self.user = User.objects.create(username='test_user')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")

    def test_get_types(self):
        response = self.client.get("/types")
        json_response = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(json_response), Type.objects.count())
        self.assertEqual(json_response[0]["label"], "Dog")
        self.assertEqual(json_response[1]["label"], "Cat")
        self.assertEqual(json_response[2]["label"], "Hamster")
        
    def test_create_type(self):
        url = "/types"
        data = {
            'label': 'Bat',
          
        }

        # Initiate request and store response
        response = self.client.post(url, data, format='json')
        # Check the response status
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Optionally, you can also check the content of the response
        self.assertEqual(response.data['label'], 'Bat')
        

        # Check if the pet object is created in the database
        type = Type.objects.get(label='Bat')
        self.assertEqual(type.label,'Bat')