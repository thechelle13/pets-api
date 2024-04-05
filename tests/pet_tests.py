from rest_framework.test import APITestCase
from rest_framework import status
from petapi.models import Pet, Type
from django.contrib.auth.models import User


class PetTests(APITestCase):
    
    fixtures = ['user', 'types']
    
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='test_user', password='password')
        # Create test pet types
        self.type1 = Type.objects.create(label='Type1')
        self.type2 = Type.objects.create(label='Type2')
        # Create test pets
        self.pet1 = Pet.objects.create(name='Rocket', type=self.type1, user=self.user, image_url='https://example.com/image1.jpg')
        self.pet2 = Pet.objects.create(name='Ebony', type=self.type2, user=self.user, image_url='https://example.com/image2.jpg')

    def test_list_pets(self):
        response = self.client.get('/pets')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_pets(self):
        # Assuming there's an existing pet with ID 1 in the database
        pet_id = 1
        url = f"/pets/{pet_id}"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Optionally, you can also check the content of the response
        json_response = response.json()
        self.assertEqual(json_response["id"], pet_id)
        # Add more assertions based on your User model fields

    def test_create_pet(self):
        url = "/pets"
        data = {
            'name': 'Scotty',
            'type': self.type1.pk,
            'image_url': 'https://example.com/image3.jpg',
            'user': self.user.pk  # Include the user ID in the data
        }

        # Initiate request and store response
        response = self.client.post(url, data, format='json')
        # Check the response status
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Optionally, you can also check the content of the response
        self.assertEqual(response.data['name'], 'Scotty')
        self.assertEqual(response.data['type'], self.type1.pk)
        self.assertEqual(response.data['image_url'], 'https://example.com/image3.jpg')

        # Check if the pet object is created in the database
        pet = Pet.objects.get(name='Scotty')
        self.assertEqual(pet.user, self.user)
       

    def test_update_pet(self):
        # Assuming there's an existing pet with ID 1 in the database
        pet_id = 1
        url = f"/pets/{pet_id}"
        data = {
            "id": pet_id,  # Include the ID of the pet being updated
            "name": "Updated Name",
            "user": 1,  # Assuming user ID 1 exists
            "type": 1,  # Assuming type ID 1 exists
            "image_url": "https://example.com/updated_image.jpg"
        }

        # Initiate request and store response
        response = self.client.put(url, data, format='json')
        
        # Check the response status
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Optionally, you can check the content of the response
        pet = Pet.objects.get(id=pet_id)
        self.assertEqual(pet.name, "Updated Name")
        self.assertEqual(pet.user_id, 1)  # Ensure user ID is updated
        self.assertEqual(pet.type_id, 1)  # Ensure type ID is updated
        self.assertEqual(pet.image_url, "https://example.com/updated_image.jpg")  # Ensure image URL is updated

    def test_delete_pet(self):
        # Assuming there's an existing PPUser with ID 1 in the database
        pet_id = 1
        url = f"/pets/{pet_id}"

        # Initiate request and store response
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Check if the PPUser has been deleted
        with self.assertRaises(Pet.DoesNotExist):
            Pet.objects.get(id=pet_id)
