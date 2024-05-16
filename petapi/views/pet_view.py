from rest_framework import viewsets, status
from rest_framework import serializers
from rest_framework.response import Response
from petapi.models import Pet, Type, PetUser
from .users_view import UserSerializer
from django.contrib.auth.models import User

class PetSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=PetUser.objects.all())
    type = serializers.StringRelatedField(source='type.label', read_only=True) 
 
    
  
    
    
    class Meta:
        model = Pet
        fields = ('id', 'user','name', 'type', 'image_url')

class PetViewSet(viewsets.ViewSet):
    
    def list(self, request):
        pets = Pet.objects.filter(user=request.user.id)
      
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
        try:
           
            pet_user = PetUser.objects.get(user=request.user)
           
            if pet_user:
                type_id = request.data.get("type")
                type = Type.objects.get(pk=type_id)
                name = request.data.get("name")
                image_url = request.data.get("image_url")

                pet = Pet.objects.create(
                    user=pet_user.user,  
                    name=name,
                    image_url=image_url,
                    type=type,
                )

                serializer = PetSerializer(pet, context={"request": request})
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({"error": "PetUser does not exist for the current user."}, status=status.HTTP_404_NOT_FOUND)
        except PetUser.DoesNotExist:
            return Response({"error": "PetUser does not exist for the current user."}, status=status.HTTP_404_NOT_FOUND)
        except Type.DoesNotExist:
            return Response({"error": "Type does not exist."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    
    def update(self, request, pk=None):
        try:
            pet = Pet.objects.get(pk=pk, user=request.user)
            if not pet:
                return Response({"error": "Pet does not exist or does not belong to the current user."}, status=status.HTTP_404_NOT_FOUND)
                
            serializer = PetSerializer(pet, data=request.data, partial=True)
            if serializer.is_valid():
                # Ensure the user field remains the same
                serializer.save(user=pet.user)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Pet.DoesNotExist:
            return Response({"error": "Pet does not exist or does not belong to the current user."}, status=status.HTTP_404_NOT_FOUND)



    def destroy(self, request, pk=None):
        try:
            pet = Pet.objects.get(pk=pk)
            self.check_object_permissions(request, pet)
            pet.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Pet.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
