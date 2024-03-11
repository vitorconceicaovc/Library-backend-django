from rest_framework import serializers
from .models import *
# from .temp import *
class Book_serializer(serializers.ModelSerializer):
    url=serializers.SerializerMethodField()
    class Meta:
        model = Book
        fields = ('__all__')

    def get_url(self, obj):
        return obj.get_absolute_url()
    
class Bookinstance_serializer(serializers.ModelSerializer):
    book=Book_serializer()
    class Meta:
        model = BookInstance
        fields = ('__all__')

    def get_url(self, obj):
        return obj.get_absolute_url()
    
class Author_serializer(serializers.ModelSerializer) :
    url = serializers.SerializerMethodField()
    class Meta:
        model = Author
        fields = ('__all__')

    def get_url(self, obj):
        return obj.get_absolute_url()