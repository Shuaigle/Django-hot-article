from rest_framework import serializers
from website.models import Post
from django.contrib.auth.models import User

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('category', 'id', 'title', 'slug', 'author',
                  'excerpt', 'content', 'status')

class UserRegisterSerializer(serializers.ModelSerializer):

    username = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ('user_name', 'first_name')
        extra_kwargs = {'password': {'write_only': True}}