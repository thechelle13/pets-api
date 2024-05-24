from rest_framework import viewsets, status
from rest_framework import serializers
from rest_framework.response import Response
from petapi.models import Post, PetUser, Pet
from .users_view import PetUserSerializer
from .type_view import TypeSerializer
from .comment_view import CommentSerializer

from .pet_view import PetSerializer
from django.contrib.auth.models import User


class PostSerializer(serializers.ModelSerializer):
   
    pet_user = PetUserSerializer(many=False)
    is_owner = serializers.SerializerMethodField()
    

    pets = PetSerializer(many=True)
    comments = CommentSerializer(many=True, read_only=True)
    likes = serializers.SerializerMethodField(read_only=True)

    def get_is_owner(self, obj):
        request = self.context.get('request')
        if request:
            return request.user == obj.pet_user.user
        return False
    
    def get_likes(self, obj):
        return obj.likes.count()

    class Meta:
        model = Post
        fields = ('id', 'pet_user', 'description','sitStartDate', 'sitEndDate', "is_owner", "comments", "likes",  "pets",)
        
class PostViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        try:
            post = Post.objects.get(pk=pk)
            serializer = PostSerializer(post, context={"request": request})
            return Response(serializer.data)

        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def create(self, request):
       
        pet_user = PetUser.objects.get(user=request.user)
        
       
        description = request.data.get("description")
        sitStartDate = request.data.get("sitStartDate")
        sitEndDate = request.data.get("sitEndDate")
        pet = request.data.get("pet")
       
        approved = request.data.get("approved", False) 
        
        pet_serializer = PetSerializer(data=pet)
        if pet_serializer.is_valid():
            pet = pet_serializer.save()
        else:
            return Response(pet_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

      
        post = Post.objects.create(
            # pet_user=pet_user,
            user=pet_user.user,
            description=description,
            sitStartDate=sitStartDate,
            sitEndDate=sitEndDate,
            pet=pet,
         
            approved=approved
           
        )

      
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    # def update(self, request, pk=None):
    #     try:
    #         post = Post.objects.get(pk=pk)

            
    #         self.check_object_permissions(request, post)

    #         serializer = PostSerializer(post, data=request.data, partial=True)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data, status=status.HTTP_200_OK)

    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #     except Post.DoesNotExist:
    #         return Response(status=status.HTTP_404_NOT_FOUND)    
        
    def destroy(self, request, pk=None):
        try:
            post = Post.objects.get(pk=pk)
            self.check_object_permissions(request, post)
            post.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)

        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        