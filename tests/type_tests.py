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