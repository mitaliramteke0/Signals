from rest_framework import generics
from .models import Post
from .serializers import PostSerializer
from .permissions import IsAuthorOrSuperuserOrReadOnly
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrSuperuserOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'body', 'author__username']  # Allow filtering on title, body, and author's username

    def perform_create(self, serializer):
        # Set the author of the post to the currently authenticated user
        serializer.save(author=self.request.user)

class PostRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrSuperuserOrReadOnly]

class PostListByAuthorView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        author_id = self.kwargs.get('author_id')
        return Post.objects.filter(author=author_id)

class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        if response.status_code == 200:
            token, created = Token.objects.get_or_create(user=request.user)
            response.data['token'] = token.key
        return response
