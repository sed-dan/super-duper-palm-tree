from django.urls import path, include
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, PostSearchView

urlpatterns = [
    path("", PostListView.as_view(), name='post_list'),
    path("search/", PostSearchView.as_view(), name='post_search_list'),
    path("<int:pk>/", PostDetailView.as_view(), name='post_detail'),
    path("news/create/", PostCreateView.as_view(), name='news_create'),
    path("articles/create/", PostCreateView.as_view(), name='articles_create'),
    path("news/<int:pk>/edit/", PostUpdateView.as_view(), name='news_edit'),
    path("articles/<int:pk>/edit/", PostUpdateView.as_view(), name='articles_edit'),
    path("news/<int:pk>/delete/", PostDeleteView.as_view(), name='news_delete'),
    path("articles/<int:pk>/delete/", PostDeleteView.as_view(), name='articles_delete'),
]
