# serializers.py

from rest_framework import serializers
from.models import User, Profile, Interest, Skill

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model
    """
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'phone_number', 'address', 'profile_picture', 'bio']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['profile_picture'] = instance.profile_picture.url if instance.profile_picture else None
        return data

class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the Profile model
    """
    user = UserSerializer(read_only=True)
    followers = serializers.StringRelatedField(many=True)
    following = serializers.StringRelatedField(many=True)
    interests = serializers.StringRelatedField(many=True)
    skills = serializers.StringRelatedField(many=True)

    class Meta:
        model = Profile
        fields = ['id', 'user', 'followers', 'following', 'interests', 'kills', 'created_at', 'updated_at']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['followers'] = [user.username for user in instance.followers.all()]
        data['following'] = [user.username for user in instance.following.all()]
        data['interests'] = [interest.name for interest in instance.interests.all()]
        data['skills'] = [skill.name for skill in instance.skills.all()]
        return data

class InterestSerializer(serializers.ModelSerializer):
    """
    Serializer for the Interest model
    """
    class Meta:
        model = Interest
        fields = ['id', 'name']

class SkillSerializer(serializers.ModelSerializer):
    """
    Serializer for the Skill model
    """
    class Meta:
        model = Skill
        fields = ['id', 'name']
