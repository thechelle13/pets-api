from rest_framework import viewsets, status
from rest_framework import serializers
from rest_framework.response import Response
from petapi.models import Post


class PostSerializer(serializers.ModelSerializer):
    
    pet_user = PetUserSerializer(many=False)
    is_owner = serializers.SerializerMethodField()
    type = TypeSerializer(many=False)


    def get_is_owner(self, obj):
        # Check if the authenticated user is the owner
        return self.context["request"].user == obj.pet_user.user

    class Meta:
        model = Post
        fields = ('id', 'pet_user', 'description','city', 'sitStartDate', 'sitEndDate', )