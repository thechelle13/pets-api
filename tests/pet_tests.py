from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from petapi.models import Pet,Type
from django.contrib.auth.models import User


class PetTests(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='test_user', password='password')
        # Create test pet types
        self.type1 = Type.objects.create(name='Type1')
        self.type2 = Type.objects.create(name='Type2')
        # Create test pets
        self.pet1 = Pet.objects.create(name='Rocket', type=self.type1, user=self.user, image_url='https://example.com/image1.jpg')
        self.pet2 = Pet.objects.create(name='Ebony', type=self.type2, user=self.user, image_url='https://example.com/image2.jpg')
        # Create API client
        self.client = APITestCase()

    def test_list_pets(self):
        response = self.client.get('/pets/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2) 

    def test_retrieve_pet(self):
        response = self.client.get(f'/pets/{self.pet1.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Rocket')

    def test_create_pet(self):
        data = {
            'name': 'Scotty',
            'type': self.type1.pk,
            'image_url': 'https://example.com/image3.jpg'
        }
        response = self.client.post('/pets/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Pet.objects.count(), 3)  
        
    def test_update_pet(self):
        data = {
            'name': 'New Name',
            'type': self.type2.pk,
            'image_url': 'https://example.com/image4.jpg'
        }
        response = self.client.put(f'/pets/{self.pet1.pk}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.pet1.refresh_from_db()
        self.assertEqual(self.pet1.name, 'New Name')

    def test_delete_pet(self):
        response = self.client.delete(f'/pets/{self.pet1.pk}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Pet.objects.count(), 1) 
