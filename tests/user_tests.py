import json
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from petapi.models import Type, Post, PetUser

class UserTests(APITestCase):
    fixtures = ['user', 'token', 'petuser']

    def test_create_registration(self):
        url = "/register"
        data = {
            "username": "newuser",
            "password": "newpassword",
            "first_name": "New",
            "last_name": "User",
            "email": "newuser@email.com",
            "bio": "Sample bio",
            "city": "New City"
        }

        # Initiate request and store response
        response = self.client.post(url, data, format='json')
        # Check the response status
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

               
        # Optionally, you can also check the content of the response
        user = User.objects.get(username='newuser')
        self.assertEqual(user.email, "newuser@email.com")

        # Check the pet_user properties in database
        pet_user = PetUser.objects.get(user=user)
        self.assertEqual(pet_user.user_id, user.id)
        

    
    def test_create_login(self):
    # Define the endpoint in the API to which the request will be sent
        url = "/login"

        # Define valid login credentials
        data = {
            "username": "michelle@email.com",  
            "password": "totherow"   
        }

        # Initiate request and store response
        response = self.client.post(url, data, format='json')
        # print("Request Data:", data)
        # print("Response Content:", response.content)
        # Check the response status
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Parse the JSON response content
        json_response = response.json()
        # print("Parsed JSON Response:", json_response)
        # Check if the response contains the token key
        self.assertIn('token', json_response)

        # Check if the token value is not empty
        token = json_response.get('token')
        # print("Token:", token)
        self.assertIsNotNone(token)
        self.assertNotEqual(token, "")


    def test_retrieve_user(self):
        # Assuming there's an existing user with ID 1 in the database
        user_id = 1
        url = f"/users/{user_id}"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Optionally, you can also check the content of the response
        json_response = response.json()
        self.assertEqual(json_response["id"], user_id)
        
        
    def test_update_user(self):
    # Assuming there's an existing User with ID 1 in the database
        user_id = 1
        url = f"/users/{user_id}"
       
        data = {
            "username": "updateduser",
            "email": "updateduser@email.com",
            "first_name": "Updated",
            "last_name": "User",
            "pet_user": {
                "city": "Updated City",
                "bio": "Updated Bio",
            }
        }
        # Initiate request and store response
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Optionally, you can check the content of the response
        user = User.objects.get(id=user_id)
        pet_user = user.pet_user
        self.assertEqual(pet_user.city, "Updated City")
        self.assertEqual(pet_user.bio, "Updated Bio")

     
    def test_delete_user(self):
        # Assuming there's an existing PPUser with ID 1 in the database
        pet_user_id = 1
        url = f"/users/{pet_user_id}"

        # Initiate request and store response
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Check if the PPUser has been deleted
        with self.assertRaises(PetUser.DoesNotExist):
            PetUser.objects.get(id=pet_user_id)