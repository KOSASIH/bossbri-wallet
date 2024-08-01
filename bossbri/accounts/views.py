# views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from django.core.serializers import serialize
from django.views.decorators.http import require_http_methods
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import User, Profile
from .serializers import UserSerializer, ProfileSerializer
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm

# Login View
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password')
            return render(request, 'accounts/login.html')
    return render(request, 'accounts/login.html')

# Logout View
def logout_view(request):
    logout(request)
    return redirect('login')

# Register View
def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

# Dashboard View
@login_required
def dashboard_view(request):
    return render(request, 'accounts/dashboard.html')

# Profile View
@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html')

# Update Profile View
@login_required
def update_profile_view(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated successfully')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    return render(request, 'accounts/update_profile.html', {'user_form': user_form, 'profile_form': profile_form})

# API Views
class UserAPIListView(APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request):
        users = self.queryset.all()
        serializer = self.serializer_class(users, many=True)
        return Response(serializer.data)

class UserAPIDetailView(APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, pk):
        user = self.queryset.get(pk=pk)
        serializer = self.serializer_class(user)
        return Response(serializer.data)

class ProfileAPIListView(APIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get(self, request):
        profiles = self.queryset.all()
        serializer = self.serializer_class(profiles, many=True)
        return Response(serializer.data)

class ProfileAPIDetailView(APIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get(self, request, pk):
        profile = self.queryset.get(pk=pk)
        serializer = self.serializer_class(profile)
        return Response(serializer.data)

# JSON Response View
@require_http_methods(['GET'])
def json_response_view(request):
    data = {'message': 'Hello, World!'}
    return JsonResponse(data)

# CSV Response View
@require_http_methods(['GET'])
def csv_response_view(request):
    data = [['Name', 'Email'], ['John Doe', 'johndoe@example.com'], ['Jane Doe', 'janedoe@example.com']]
    return HttpResponse(content_type='text/csv', headers={'Content-Disposition': 'attachment; filename="users.csv"'}, body='\n'.join([','.join(row) for row in data]))
