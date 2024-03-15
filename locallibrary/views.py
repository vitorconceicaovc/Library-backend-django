from typing import Any
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import BasicAuthentication, SessionAuthentication

@api_view(['POST'])
@permission_classes([AllowAny])  # Permitir acesso sem autenticação
def register_user(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({'error': 'Username and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

        # Verificar se o usuário já existe
        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username is already taken.'}, status=status.HTTP_400_BAD_REQUEST)

        # Criar um novo usuário
        user = User.objects.create_user(username=username, password=password)
        user.save()

        return Response({'success': 'User registered successfully.'}, status=status.HTTP_201_CREATED)

    return Response({'error': 'Invalid request method.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from rest_framework import status

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    data = {
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
    }
    return Response(data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_list(request):
    users = User.objects.all()
    data = {
        'users': list(users.values())
    }
    return Response(data)

class REST_self_user(APIView):
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        user = request.user
        print(f"Rest User: {user}")


        response_data = {
            "status": True,
            "code": "",
            "data": {
                "user_id": user.id,
                "username": user.username,
                "first_name" : user.first_name,
                "last_name" : user.last_name,
                "email": user.email,
            },
            "admin": user.is_superuser
        }
        return Response(response_data)
