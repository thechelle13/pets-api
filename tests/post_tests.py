import json
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from petapi.models import Post, PetUser

class PostTests(APITestCase):
    fixtures = ['user', 'petuser', 'token', 'comments']
    
    def setUp(self):
        self.user = User.objects.get(username='michelle@email.com')
        self.pet_user = PetUser.objects.get(user=self.user)
        self.token = Token.objects.get(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")
        
    def test_retrieve_posts(self):
        # Ensure we can retrieve an existing post
        url = "/posts"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    # def test_create_post(self):
    #     url = "/posts"
    #     data = {
    #         'description': 'New Post',
    #         'sitStartDate': '2024-04-16',
    #         'sitEndDate': '2024-04-20',
    #         'pet_id': 1,
    #         'approved': True
    #     }
        
    #     # Ensure that the request object is passed to the serializer context
    #     response = self.client.post(url, data, format='json', HTTP_AUTHORIZATION=f"Token {self.token.key}")

    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertIn('id', response.data)
    #     self.assertEqual(response.data['description'], 'New Post')

    # def test_delete_post(self):
    #     post_id = Post.objects.first().id  
    #     url = f"/posts/{post_id}/"
    #     # Ensure that the request object is passed to the delete view
    #     response = self.client.delete(url, HTTP_AUTHORIZATION=f"Token {self.token.key}")
    #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

