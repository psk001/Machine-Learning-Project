from rest_framework import serializers
from .models import Author

class AuthorSerializer(serializers.Serializer):   
    name = serializers.CharField(max_length=200)
    email = serializers.EmailField()


        # class Meta:
        # model=Author
        # fields = '__all__' 