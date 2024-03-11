from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from .models import BookInstance
from .models import Author
from django.contrib.auth.models import User

class REST_list_books(APIView):
    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    #permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        # user_id=request.GET.get('id')
        # # print(f'USER ID: {user_id}')
        # user=User.objects.get(id=user_id)
        # print(user)
        books=BookInstance.objects.all()
        # print(request.user, request.user.is_authenticated, request.user.is_superuser)
        # print(user.bookinstance_set.all())
        data=Bookinstance_serializer(books, many=True).data
        return Response({"status":True,"code":"","data":data})
    
class REST_list_authors(APIView):

    def get(self, request, format=None):
        authors=Author.objects.all()
        data=Author_serializer(authors, many=True).data
        return Response({"status":True,"code":"","data":data})
    
