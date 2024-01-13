from rest_framework import viewsets, status
from rest_framework import serializers
from rest_framework.response import Response
from petapi.models import Pet

class PetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pet
        fields = ('id', 'name', 'type', "image_url" )
        
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
        # Get the data from the client's JSON payload
        name = request.data.get("name")
        image_url = request.data.get("image_url")
        type = request.data.get("type")

        # Create a comment database row first, so you have a
        # primary key to work with
        pet = Pet.objects.create(
            name=name,
            image_url=image_url,
            type=type,
        )

        serializer = PetSerializer(pet, context={"request": request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        try:
            pet = Pet.objects.get(pk=pk)

            # Is the authenticated user allowed to edit this tag?
            self.check_object_permissions(request, pet)

            serializer = PetSerializer(data=request.data)
            if serializer.is_valid():
                pet.name = serializer.validated_data["name"]
                pet.type = serializer.validated_data["type"]
                pet.image_url = serializer.validated_data["image_url"]
                pet.save()

                serializer = PetSerializer(pet, context={"request": request})
                return Response(None, status.HTTP_204_NO_CONTENT)

            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

        except pet.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            pet = Pet.objects.get(pk=pk)
            self.check_object_permissions(request, pet)
            pet.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)

        except pet.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
