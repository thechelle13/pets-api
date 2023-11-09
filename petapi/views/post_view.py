from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from petapi.models import Post


class PostView(ViewSet):

    def retrieve(self, request, pk=None):
        # Step 1: Get a single post based on the primary key in the request URL
        post = Post.objects.get(pk=pk)

        # Step 2: Serialize the post record as JSON
        serialized = PostSerializer(post, many=False)

        # Step 3: Send JSON response to client with 200 status code
        return Response(serialized.data, status=status.HTTP_200_OK)

    def list(self, request):
        # Step 1: Get all post data from the database
        posts = Post.objects.all()

        # Step 2: Convert the data to JSON format
        serialized = PostSerializer(posts, many=True)

        # Step 3: Respond to the client with the JSON data and 200 status code
        return Response(serialized.data, status=status.HTTP_200_OK)


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'description','city', 'sitStartDate', 'sitEndDate', )