import requests
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .forms import UserRegisterForm, UserLoginForm, TaskForm


# User Registration
def register_user(request):
    form = UserRegisterForm(request.POST)
    if request.method == 'POST':

        data = {
            'username': request.POST.get('username'),
            'password1': request.POST.get('password1'),
            'password2': request.POST.get('password2'),
        }
        response = requests.post(f'{settings.USER_SERVICE_URL}/accounts/register/', json=data)
        if response.status_code == 201:
            return redirect('login')
    return render(request, 'frontend/register.html', {'form': form})


# User Login
def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)

        data = form.cleaned_data
        response = requests.post(f'{settings.USER_SERVICE_URL}/accounts/login/', json=data)
        if response.status_code == 200:
            user_data = response.json()  # Assume the response contains session data
            # Implement session login here if necessary
            return redirect('task_list')

    return render(request, 'frontend/login.html', {'form': form})


# User Logout
@login_required
def user_logout(request):
    response = requests.post(f'{settings.USER_SERVICE_URL}/accounts/logout/')
    if response.status_code == 200:
        logout(request)  # Log out the user from Django session
        return redirect('login')
    return JsonResponse({'error': 'Logout failed'}, status=400)


# Create Task
@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)

        task_data = form.cleaned_data
        task_data['user'] = request.user.id  # Add user ID to task data
        response = requests.post(f'{settings.TASK_SERVICE_URL}/api/tasks/', json=task_data)
        if response.status_code == 201:
            return redirect('task_list')

    return render(request, 'frontend/task_form.html', {'form': form})


# Task List
@login_required
def task_list(request):
    response = requests.get(f'{settings.TASK_SERVICE_URL}/api/tasks/', params={'user': request.user.id})
    if response.status_code == 200:
        tasks = response.json()
    else:
        tasks = []
    return render(request, 'frontend/task_list.html', {'tasks': tasks})


# Task Detail
@login_required
def task_detail(request, task_id):
    response = requests.get(f'{settings.TASK_SERVICE_URL}/api/tasks/{task_id}/', params={'user': request.user.id})
    if response.status_code == 200:
        task = response.json()
        return render(request, 'frontend/task_detail.html', {'task': task})
    else:
        return JsonResponse({'error': 'Task not found'}, status=404)


# Update Task
@login_required
def task_update(request, task_id):
    if request.method == 'POST':
        task_data = {
            'title': request.POST.get('title'),
            'description': request.POST.get('description'),
            'completed': request.POST.get('completed')
        }
        response = requests.put(f'{settings.TASK_SERVICE_URL}/api/tasks/{task_id}/', json=task_data)
        if response.status_code == 200:
            return redirect('task_list')
    else:
        response = requests.get(f'{settings.TASK_SERVICE_URL}/api/tasks/{task_id}/', params={'user': request.user.id})
        task = response.json() if response.status_code == 200 else {}
    return render(request, 'frontend/task_form.html', {'task': task})


# Delete Task
@login_required
def task_delete(request, task_id):
    if request.method == 'POST':
        response = requests.delete(f'{settings.TASK_SERVICE_URL}/api/tasks/{task_id}/')
        if response.status_code == 204:
            return redirect('task_list')
    return render(request, 'frontend/task_confirm_delete.html', {'task_id': task_id})
