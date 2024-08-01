# views.py

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import User, Profile
from .serializers import UserSerializer, ProfileSerializer
from .permissions import IsOwnerOrReadOnly

class UserAPIListView(APIView):
    """
    API view for listing all users
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request):
        users = self.queryset.all()
        serializer = self.serializer_class(users, many=True)
        return Response(serializer.data)

class UserAPIDetailView(APIView):
    """
    API view for retrieving a single user instance
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, pk):
        user = self.queryset.get(pk=pk)
        serializer = self.serializer_class(user)
        return Response(serializer.data)

class ProfileAPIListView(APIView):
    """
    API view for listing all profiles
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get(self, request):
        profiles = self.queryset.all()
        serializer = self.serializer_class(profiles, many=True)
        return Response(serializer.data)

class ProfileAPIDetailView(APIView):
    """
    API view for retrieving a single profile instance
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get(self, request, pk):
        profile = self.queryset.get(pk=pk)
        serializer = self.serializer_class(profile)
        return Response(serializer.data)

    def put(self, request, pk):
        profile = self.queryset.get(pk=pk)
        serializer = self.serializer_class(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        profile = self.queryset.get(pk=pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
