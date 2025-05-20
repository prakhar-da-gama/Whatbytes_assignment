from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def RegisterView(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')
    if not all([username, email, password]):
        return Response({'error': 'Missing fields'}, status=400)
    if User.objects.filter(username=username).exists():
        return Response({'error': 'User exists'}, status=400)
    user = User.objects.create_user(username=username, email=email, password=password)
    return Response({'message': 'User registered successfully'}, status=201)
