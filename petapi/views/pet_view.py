from rest_framework import viewsets, status
from rest_framework import serializers
from rest_framework.response import Response
from petapi.models import Pet

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ('id', 'user','name', 'type', 'image_url')

class PetViewSet(viewsets.ViewSet):
    def list(self, request):
        pets = Pet.objects.all()
        serializer = PetSerializer(pets, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            pet = Pet.objects.get(pk=pk)
            serializer = PetSerializer(pet)
            return Response(serializer.data)
        except Pet.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = PetSerializer(data=request.data)
        if serializer.is_valid():
            pet = serializer.save()  # Using serializer.save() to create the object
            return Response(PetSerializer(pet).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            pet = Pet.objects.get(pk=pk)
            self.check_object_permissions(request, pet)
            serializer = PetSerializer(pet, data=request.data)
            if serializer.is_valid():
                serializer.save()  # Using serializer.save() to update the object
                return Response(status=status.HTTP_204_NO_CONTENT)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Pet.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            pet = Pet.objects.get(pk=pk)
            self.check_object_permissions(request, pet)
            pet.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Pet.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
