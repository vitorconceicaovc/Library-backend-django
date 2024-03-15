from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import * 
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import BookInstance
from .models import Author
from django.contrib.auth.models import User
from rest_framework import status

class REST_list_books_instances(APIView):
    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    #permission_classes = (IsAuthenticated,)
    permission_classes=()

    def get(self, request, format=None):
        # user_id=request.GET.get('id')
        # # print(f'USER ID: {user_id}')
        # user=User.objects.get(id=user_id)
        # print(user)
        books=BookInstance.objects.all()
        # print(request.user, request.user.is_authenticated, request.user.is_superuser)
        # print(user.bookinstance_set.all())
        data=Bookinstance_serializer(books, many=True).data
        return Response({"status":True,"code":"","data":data, "admin":request.user.is_superuser})
class REST_list_self_books_instances(APIView):
    authentication_classes = [JWTAuthentication,SessionAuthentication]
    permission_classes = (IsAuthenticated,)
    #permission_classes=()

    def get(self, request, format=None):
        # user_id=request.GET.get('id')
        # # print(f'USER ID: {user_id}')
        user=request.user
        print(user)
        books=BookInstance.objects.filter(borrower=user)
        # print(request.user, request.user.is_authenticated, request.user.is_superuser)
        # print(user.bookinstance_set.all())
        data=Bookinstance_serializer(books, many=True).data
        return Response({"status":True,"code":"","data":data,"admin":request.user.is_superuser})
class REST_list_authors(APIView):
    permission_classes=()

    def get(self, request, format=None):
        authors=Author.objects.all()
        data=Author_serializer(authors, many=True).data
        return Response({"status":True,"code":"","data":data,"admin":request.user.is_superuser})
    
class REST_list_books(APIView):
    permission_classes=()

    def get(self, request, format=None):
        books=Book.objects.all()
        data=Book_serializer(books, many=True).data
        return Response({"status":True,"code":"","data":data})
    
class REST_book_detail(APIView):
    permission_classes=()
    def get(self, request, pk, format=None):
        book = self.get_object(pk)
        serializer = Book_serializer(book)
        return Response(serializer.data)

    def get_object(self,pk):
        return Book.objects.get(id=pk)
    
class REST_author_detail(APIView):
    permission_classes=()
    def get(self, request, pk, format=None):
        author = self.get_object(pk)
        serializer = Author_serializer(author)
        return Response(serializer.data)

    def get_object(self,pk):
        return Author.objects.get(id=pk)

class REST_author_detail_jwt_auth(APIView):
    authentication_classes=[JWTAuthentication,]
    permission_classes=(IsAuthenticated,)

    def get(self, request, pk, format=None):
        author = self.get_object(pk)
        serializer = Author_serializer(author)
        return Response(serializer.data)

    def get_object(self,pk):
        return Author.objects.get(id=pk)
 
class RequestsAPIView(APIView):
    serializer_class = RequestSerializer

    def get(self, request, pk=None):
        requests = Requests.objects.all()
        serializer = RequestSerializer(requests, many=True)
        return Response(serializer.data)
    
    def get_object(self,pk):
        return Author.objects.get(id=pk)

    def post(self, request):
        print(request.POST, request.data)
        data=request.data.copy()
        data["user"]=request.user.id
        serializer = RequestSerializer_form(data=data)
        if serializer.is_valid():
            obj=serializer.save()
            return Response(RequestSerializer(instance=obj).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class RequestDetailAPIView(APIView):
    permission_classes=()
    def get(self, request, pk, format=None):
        request = self.get_object(pk)
        serializer = RequestSerializer(request)
        return Response(serializer.data)

    def get_object(self,pk):
        return Requests.objects.get(id=pk)
    
    def put(self, request, pk):
        request_obj = self.get_object(pk)
        print(request.data, request_obj)
        resp,msg=request_obj.set_state(request.data['status'])
        serializer = RequestSerializer(instance=request_obj)
        return Response({'status':resp, 'msg':msg})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
