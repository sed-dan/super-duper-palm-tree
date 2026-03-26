from django.urls import path, include
from .views import PostListView, PostDetailView


urlpatterns = [
    path("", PostListView.as_view(), name='post_list'),
    path("<int:pk>/", PostDetailView.as_view(), name='post_detail'),
]
