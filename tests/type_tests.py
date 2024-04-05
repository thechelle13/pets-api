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
        
        
    def test_retrieve_types(self):
        # Assuming there's an existing pet with ID 1 in the database
        type_id = 1
        url = f"/types/{type_id}"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Optionally, you can also check the content of the response
        json_response = response.json()
        self.assertEqual(json_response["id"], type_id)
      

         
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
        
        
    def test_update_type(self):
        # Assuming there's an existing pet with ID 1 in the database
        type_id = 1
        url = f"/types/{type_id}"
        data = {
            "id": type_id,  # Include the ID of the pet being updated
            "label": "Updated Type",
           
        }

        # Initiate request and store response
        response = self.client.put(url, data, format='json')
        
        # Check the response status
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Optionally, you can check the content of the response
        type = Type.objects.get(id=type_id)
        self.assertEqual(type.label, "Updated Type")
    
        
        
    def test_delete_type(self):
        # Assuming there's an existing PPUser with ID 1 in the database
        type_id = 1
        url = f"/types/{type_id}"

        # Initiate request and store response
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Check if the PPUser has been deleted
        with self.assertRaises(Type.DoesNotExist):
            Type.objects.get(id=type_id)