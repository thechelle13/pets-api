from rest_framework import viewsets, status
from rest_framework import serializers
from rest_framework.response import Response
from petapi.models import Type

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ["id", "label"]

class TypeViewSet(viewsets.ViewSet):
    def list(self, request):
        types = Type.objects.all()
        serializer = TypeSerializer(types, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            type = Type.objects.get(pk=pk)
            serializer = TypeSerializer(type)
            return Response(serializer.data)
        except Type.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def create(self, request):
        serializer = TypeSerializer(data=request.data)
        if serializer.is_valid():
            type = serializer.save()  # Using serializer.save() to create the object
            return Response(TypeSerializer(type).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def update(self, request, pk=None):
        try:
            type = Type.objects.get(pk=pk)
            # Is the authenticated user allowed to edit this tag?
            self.check_object_permissions(request, type)

            serializer = TypeSerializer(data=request.data)
            if serializer.is_valid():
                type.label = serializer.validated_data["label"]
                type.save()

                serializer = TypeSerializer(type, context={"request": request})
                return Response(None, status.HTTP_204_NO_CONTENT)

            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

        except type.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            type = Type.objects.get(pk=pk)
            self.check_object_permissions(request, type)
            type.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)

        except type.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    

  