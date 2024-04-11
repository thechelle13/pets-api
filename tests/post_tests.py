import json
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from petapi.models import Post, PetUser

# class PostTests(APITestCase):
#     fixtures = ['user', 'petuser', 'token', 'comments', 'pets']
    
#     def setUp(self):
#         self.user = User.objects.get(username='michelle@email.com')
#         self.pet_user = PetUser.objects.get(user=self.user)
#         self.token = Token.objects.get(user=self.user)
#         self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")

    # def test_create_event(self):
    #     url = "/posts"
    #     data = {
    #         'description': 'New Post',
    #         'sitStartDate': '2024-04-16',
    #         'sitEndDate': '2024-04-20',
    #         'pet': 1,
    #         'pet_user': 1,
    #         'approved': True,
    #         'publication_date': '2024-04-09'
    #     }
        
    #     response = self.client.post(url, data, format='json')

    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    #     json_response = response.json()
    #     self.assertEqual(json_response["id"], 1) 
    #     self.assertEqual(json_response["description"], "New Post")
    #     self.assertEqual(json_response["sitStartDate"], "2024-04-16")
    #     self.assertEqual(json_response["sitEndDate"], "2024-04-20")

    # def test_retrieve_posts(self):
    #     url = "/posts"
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_update_posts(self):
    #     post_id = Post.objects.first().id
    #     url = f"/posts/{post_id}/"
    #     data = {
    #         'description': 'Updated Description',
    #     }
    #     response = self.client.put(url, data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(response.data['description'], 'Updated Description')

    # def test_delete_post(self):
    #     post_id = Post.objects.first().id  
    #     url = f"/posts/{post_id}/"
    #     response = self.client.delete(url)
    #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
class PostTests(APITestCase):
    fixtures = ['user', 'petuser', 'token', 'comments', 'pets']
    
    def setUp(self):
        self.user = User.objects.get(username='michelle@email.com')
        self.pet_user = PetUser.objects.get(user=self.user)
        self.token = Token.objects.get(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")

    def test_create_post(self):
        url = "/posts"
        data = {
            'description': 'New Post',
            'sitStartDate': '2024-04-16',
            'sitEndDate': '2024-04-20',
            'pet_id': 1,
            'approved': True
        }
        
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('id', response.data)
        self.assertEqual(response.data['description'], 'New Post')

    def test_delete_post(self):
        post_id = Post.objects.first().id  
        url = f"/posts/{post_id}/"
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
