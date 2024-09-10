
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.middleware.csrf import get_token

# API View for User Registration
@csrf_exempt  # If you're using APIs without CSRF tokens for simplicity
def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        if User.objects.filter(username=username).exists():
            return JsonResponse({'error': 'Username already exists'}, status=400)
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return JsonResponse({'message': 'User registered successfully'})
    return JsonResponse({'error': 'Invalid request method'}, status=400)

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
