# serializers.py

from rest_framework import serializers
from .models import User, Profile

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'phone_number', 'address', 'profile_picture', 'bio', 'is_active', 'is_admin', 'created_at', 'updated_at']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['profile_picture'] = instance.profile_picture.url if instance.profile_picture else None
        return data

# Profile Serializer
class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ['id', 'user', 'followers', 'following', 'interests', 'skills', 'created_at', 'updated_at']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['followers'] = [user.username for user in instance.followers.all()]
        data['following'] = [user.username for user in instance.following.all()]
        return data

# User Registration Serializer
class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'phone_number', 'address', 'password', 'password_confirm']

    def validate(self, data):
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError('Passwords do not match')
        return data

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone_number=validated_data['phone_number'],
            address=validated_data['address']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

# Profile Update Serializer
class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['interests', 'skills', 'profile_picture']

    def update(self, instance, validated_data):
        instance.interests = validated_data.get('interests', instance.interests)
        instance.skills = validated_data.get('skills', instance.skills)
        instance.profile_picture = validated_data.get('profile_picture', instance.profile_picture)
        instance.save()
        return instance
