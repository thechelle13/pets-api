from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from petapi.models import Pet


class PetView(ViewSet):

    def retrieve(self, request, pk=None):
        # Step 1: Get a single dog based on the primary key in the request URL
        pet = Pet.objects.get(pk=pk)

        # Step 2: Serialize the dog record as JSON
        serialized = PetSerializer(pet, many=False)

        # Step 3: Send JSON response to client with 200 status code
        return Response(serialized.data, status=status.HTTP_200_OK)

    def list(self, request):
        # Step 1: Get all dog data from the database
        pets = Pet.objects.all()

        # Step 2: Convert the data to JSON format
        serialized = PetSerializer(pets, many=True)

        # Step 3: Respond to the client with the JSON data and 200 status code
        return Response(serialized.data, status=status.HTTP_200_OK)


class PetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pet
        fields = ('id', 'name', 'type', )
