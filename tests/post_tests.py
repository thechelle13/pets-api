# import json
# from rest_framework import status
# from rest_framework.test import APITestCase
# from django.contrib.auth.models import User
# from rest_framework.authtoken.models import Token
# from petapi.models import Post

# class PostTests(APITestCase):

#     fixtures = ['posts', 'user']

#     def setUp(self):
#         self.user = User.objects.create(username='test_user')
#         self.token = Token.objects.create(user=self.user)
#         self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")

#     def test_get_posts(self):
#         response = self.client.get("/posts")
#         json_response = response.json()

#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(json_response), Post.objects.count())

#     def test_retrieve_post(self):
#         post = Post.objects.first()
#         response = self.client.get(f"/posts/{post.pk}/")
#         json_response = response.json()

#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(json_response['description'], post.description)
#         # Add more assertions based on your Post model fields

#     def test_create_post(self):
#         data = {
#             'description': 'Sample post description',
#             'sitStartDate': '2023-01-15',
#             'sitEndDate': '2023-01-20',
#             'pet': 1, 
#             'pet_user': 1, 
#             'approved': True,
#             'publication_date': '2023-01-01'
#         }
#         response = self.client.post("/posts/", data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Post.objects.count(), 5)  

#     def test_update_post(self):
#         post = Post.objects.first()
#         data = {
#             'description': 'Updated description',
#             'sitStartDate': '2023-01-15',
#             'sitEndDate': '2023-01-20',
#             'pet': post.pet.pk, 
#             'pet_user': post.pet_user.pk,  
#             'approved': True,
#             'publication_date': '2023-01-01'
#         }
#         response = self.client.put(f"/posts/{post.pk}/", data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         post.refresh_from_db()
#         self.assertEqual(post.description, 'Updated description')

#     def test_delete_post(self):
#         post = Post.objects.first()
#         response = self.client.delete(f"/posts/{post.pk}/")
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#         self.assertEqual(Post.objects.count(), 3)  

# from rest_framework.test import APITestCase
# from rest_framework import status
# from django.contrib.auth.models import User
# from rest_framework.authtoken.models import Token
# from petapi.models import Post

# class PostTests(APITestCase):
    
#     fixtures = ['petuser', 'posts']  # Assuming you have fixture files for users and posts
    
#     def setUp(self):
#         # Assuming you have a user fixture with username 'test_user'
#         self.user = User.objects.get(username='test_user')
#         self.token = Token.objects.create(user=self.user)
#         self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")

    
#     def test_list_posts(self):
#         response = self.client.get('/posts')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         # Assuming there are 4 posts in the fixture
#         self.assertEqual(len(response.data), 4)

