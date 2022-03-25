from django.shortcuts import get_object_or_404
from rest_framework import generics
from website.models import Post
from .serializers import PostSerializer
from rest_framework import viewsets
from rest_framework.permissions import BasePermission, SAFE_METHODS,IsAuthenticated, AllowAny, IsAdminUser

class PostUserWritePermission(BasePermission):
    message = 'Editing posts is restricted to the author only.'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        
        return obj.author == request.user

class PostList(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Post, slug=item)

    def get_queryset(self):
        return Post.objects.all()

# class PostDetail(generics.RetrieveAPIView, PostUserWritePermission):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

#     def get_object(self, queryset=None, **kwargs):
#         item = self.kwards.get('pk')
#         return get_object_or_404(Post, slug=item)

