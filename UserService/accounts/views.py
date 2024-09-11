from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.middleware.csrf import get_token
import time

from .metrics import track_request, track_latency


# API View for User Registration
@api_view(['POST'])
def register_user(request):
    start_time = time.time()
    track_request(request.method, '/register')
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password1')
        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        csrf_token = get_token(request)
        duration = time.time() - start_time
        track_latency(duration)        # Generate CSRF token after login
        return Response({'message': 'User registered successfully', 'csrfToken': csrf_token}, status=status.HTTP_201_CREATED)
    return Response({'error': 'Invalid request method'}, status=status.HTTP_400_BAD_REQUEST)

# API View for User Login
@api_view(['POST'])
def login_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
        login(request, user)
        csrf_token = get_token(request)
        return Response({'message': 'Login successful', 'csrfToken': csrf_token}, status=status.HTTP_200_OK)
    return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

# API View for User Logout
@api_view(['POST'])
def logout_user(request):
    logout(request)
    return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)
