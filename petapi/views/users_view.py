from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from petapi.models import PetUser

class PetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetUser
        fields = ("id", "user", "active", "bio", "city")

class UserSerializer(serializers.ModelSerializer):
    pet_user = PetUserSerializer(many=False, read_only=True)  

    class Meta:
        model = User
        fields = ["id", "username", "password", "first_name", "last_name", "email", "pet_user"]
        extra_kwargs = {"password": {"write_only": True}}
        
class UserViewSet(viewsets.ViewSet):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer

    @action(detail=False, methods=["get"], url_path="petusers")
    def get_pet_users(self, request):
        # Ensure the user is authenticated
        if not request.user.is_authenticated:
            return Response(
                {"error": "Authentication required"},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        # Filter PetUser objects for the current authenticated user
        pet_users = PetUser.objects.filter(user=request.user)
        serializer = PetUserSerializer(pet_users, many=True)
        

        # Check if the PetUser exists
        if pet_users.exists():
            return Response(serializer.data, status=status.HTTP_200_OK)
       
        
        else:
            return Response(
                {"error": "PetUser not found"}, status=status.HTTP_404_NOT_FOUND
            )
            
    def list(self, request):
        users = User.objects.all()  
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        try:
            user_instance = User.objects.get(pk=pk)
            serializer = UserSerializer(user_instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

 
    def update(self, request, pk=None):
        try:
            user_instance = User.objects.get(pk=pk)

            # Is the authenticated user allowed to edit this user?
            self.check_object_permissions(request, user_instance)

            # Update User model fields
            user_instance.email = request.data.get('email', user_instance.email)
            user_instance.first_name = request.data.get('first_name', user_instance.first_name)
            user_instance.last_name = request.data.get('last_name', user_instance.last_name)
            # Update other fields if needed

            # Save User instance
            user_instance.save()

            # Parse pet_user data from request
            pet_user_data = request.data.get('pet_user', {})

            # Update PetUser model fields
            pet_user = user_instance.pet_user
            pet_user.city = pet_user_data.get('city', pet_user.city)
            pet_user.bio = pet_user_data.get('bio', pet_user.bio)
            # Update other fields if needed

            # Save PetUser instance
            pet_user.save()

            serializer = UserSerializer(user_instance, context={"request": request})
            return Response(serializer.data, status=status.HTTP_200_OK)

        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        
    # def update(self, request, pk=None):
    #     try:
    #         user_instance = User.objects.get(pk=pk)

    #         # Is the authenticated user allowed to edit this user?
    #         self.check_object_permissions(request, user_instance)

    #         # Parse pet_user data from request
    #         pet_user_data = request.data.get('pet_user', {})

    #         # Update PetUser model fields
    #         pet_user = user_instance.pet_user
    #         pet_user.city = pet_user_data.get('city', pet_user.city)
    #         pet_user.bio = pet_user_data.get('bio', pet_user.bio)
    #         # Update other fields if needed

    #         # Save PetUser instance
    #         pet_user.save()

    #         serializer = UserSerializer(user_instance, context={"request": request})
    #         return Response(serializer.data, status=status.HTTP_200_OK)

    #     except User.DoesNotExist:
    #         return Response(status=status.HTTP_404_NOT_FOUND)

        
    def destroy(self, request, pk=None):
        try:
            user_instance = User.objects.get(pk=pk)

            self.check_object_permissions(request, user_instance)

            user_instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=["post"], url_path="register")
    def register_account(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.create_user(
                username=serializer.validated_data["username"],
                password=serializer.validated_data["password"],
                first_name=serializer.validated_data["first_name"],
                last_name=serializer.validated_data["last_name"],
                # city=serializer.validated_data["city"],
                email=serializer.validated_data["email"],
            )
            pet_user = PetUser.objects.create(
                user=user,
                active=True,
                bio=request.data.get("bio"),
                city=request.data.get("city"),
            )
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=["post"], url_path="login")
    def user_login(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)

        if user:
            token = Token.objects.get(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        else:
            return Response(
                {"error": "Invalid Credentials"}, status=status.HTTP_400_BAD_REQUEST
            )