from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.PostListCreateView.as_view(), name='post-list'),
    path('posts/<int:pk>/', views.PostRetrieveUpdateDeleteView.as_view(), name='post-detail'),
    path('posts/by_author/<int:author_id>/', views.PostListByAuthorView.as_view(), name='post-list-by-author'),
    path('token/', views.CustomObtainAuthToken.as_view(), name='token-obtain'),
]
