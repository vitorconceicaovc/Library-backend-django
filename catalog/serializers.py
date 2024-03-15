from rest_framework import serializers
from .models import *
# from .temp import *

class Author_serializer(serializers.ModelSerializer) :
    url = serializers.SerializerMethodField()
    class Meta:
        model = Author
        fields = ('__all__')

    def get_url(self, obj):
        return obj.get_absolute_url()
    
class Book_serializer(serializers.ModelSerializer):
    url=serializers.SerializerMethodField()  
    author = Author_serializer()  
    language = serializers.StringRelatedField()
    genre = serializers.StringRelatedField(many=True)

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

class RequestSerializer(serializers.ModelSerializer):
    # Definindo campos customizados para incluir as informações do livro e do usuário
    book = Book_serializer()
    user = serializers.SerializerMethodField()

    class Meta:
        model = Requests
        fields = '__all__'

    def get_user(self, obj):
        # Obtendo o objeto de usuário associado ao pedido
        user_instance = obj.user
        # Serializando o objeto de usuário como necessário (por exemplo, apenas o nome de usuário)
        # Se você quiser mais informações, você pode criar um UserSerializer
        user_data = {
            'id': user_instance.id,
            'first_name': user_instance.first_name,
            'last_name': user_instance.last_name,
            'email': user_instance.email,
            # Adicione outros campos do usuário que desejar
        }
        return user_data

    def get_url(self, obj):
        return obj.get_absolute_url()
        
class RequestSerializer_form(serializers.ModelSerializer):
    # Definindo campos customizados para incluir as informações do livro e do usuário
    #book = serializers.SerializerMethodField()
    #user = serializers.SerializerMethodField()

    class Meta:
        model = Requests
        fields = '__all__'