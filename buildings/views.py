from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Buildings, Files
from .serializers import BuildingsSerializer, FilesSerializer


class BuildingsList(APIView):
    """
    BuildingsList
    """
    def get(self, request, format=None):
        buildings = Buildings.objects.all()
        serializer = BuildingsSerializer(buildings, many=True)
        return Response(serializer.data)

    # def post(self, request, format=None):
    #     serializer = SnippetSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FilesList(APIView):
    """
    FilesList
    """
    def get(self, request, format=None):
        files = Files.objects.all()
        serializer = FilesSerializer(files, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        print(request.data)

        serializer = FilesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
