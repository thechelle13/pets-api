from rest_framework import viewsets, status
from rest_framework import serializers
from rest_framework.response import Response
from petapi.models import Post, PetUser, Comment
from .users_view import PetUserSerializer
from .type_view import TypeSerializer
from .comment_view import CommentSerializer



class PostSerializer(serializers.ModelSerializer):
    pet_user = PetUserSerializer(read_only=True)
    is_owner = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, read_only=True)
    likes = serializers.SerializerMethodField(read_only=True) 

    def get_is_owner(self, obj):
        request = self.context.get('request')
        if request:
            return request.user == obj.pet_user.user
        return False
    
    def get_likes(self, obj):
        # Return number of likes for the post
        return obj.likes.count()

    class Meta:
        model = Post
        fields = ('id', 'pet_user', 'description','sitStartDate', 'sitEndDate', "is_owner", 'comments', 'likes', )
        
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
        # Retrieve pet_user object associated with the authenticated user
        pet_user = PetUser.objects.get(user=request.user)
        
        # Extract necessary fields from request data
        description = request.data.get("description")
        sit_start_date = request.data.get("sitStartDate")
        sit_end_date = request.data.get("sitEndDate")
        pet_id = request.data.get("pet_id")
       
        approved = request.data.get("approved", False) 

        # Create the post object
        post = Post.objects.create(
            pet_user=pet_user,
            description=description,
            sitStartDate=sit_start_date,
            sitEndDate=sit_end_date,
            pet_id=pet_id,
         
            approved=approved
           
        )

        # Serialize the created post object and return the serialized data in the response
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    def update(self, request, pk=None):
        try:
            post = Post.objects.get(pk=pk)

            # Is the authenticated user allowed to edit this post?
            self.check_object_permissions(request, post)

            serializer = PostSerializer(post, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)    
        
    def destroy(self, request, pk=None):
        try:
            post = Post.objects.get(pk=pk)
            self.check_object_permissions(request, post)
            post.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)

        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        