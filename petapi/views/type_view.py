from rest_framework import viewsets, status
from rest_framework import serializers
from rest_framework.response import Response
from petapi.models import Type
from rest_framework.permissions import AllowAny 

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
            type = serializer.save() 
            return Response(TypeSerializer(type).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    
    def update(self, request, pk=None):
        try:
            type = Type.objects.get(pk=pk)
            self.check_object_permissions(request, type)

            serializer = TypeSerializer(type, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Type.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)



    def destroy(self, request, pk=None):
        try:
            type = Type.objects.get(pk=pk)
            self.check_object_permissions(request, type)
            type.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)

        except type.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    

  