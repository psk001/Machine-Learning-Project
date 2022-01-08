from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Author
from .serializers import AuthorSerializer

# Create your views here.

class AuthorView(APIView):
    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
       
        return Response({"authors": serializer.data})
