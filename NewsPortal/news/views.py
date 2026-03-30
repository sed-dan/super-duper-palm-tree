from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .utils import create_or_edit

from .forms import PostForm
from .models import Post
from django_filters.views import FilterView
from .filters import PostFilter

class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'news/post_list.html'
    ordering = ['-post_date']
    paginate_by = 10

class PostSearchView(FilterView):
    model = Post
    context_object_name = 'posts'
    template_name = 'news/post_search_list.html'
    ordering = ['-post_date']
    paginate_by = 10
    filterset_class = PostFilter

class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'news/post_detail.html'

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'news/post_create_or_edit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        path_create = reverse_lazy('post_create')
        return create_or_edit(context, self.request.path)

    def form_valid(self, form):
        if self.request.path == "/post/news/create/":
            post = form.save(commit=False)
            post.article_news = "N"
            return super().form_valid(form)
        else:
            post = form.save(commit=True)
            return super().form_valid(form)


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'news/post_create_or_edit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return create_or_edit(context, self.request.path)

class PostDeleteView(DeleteView):
    model = Post
    context_object_name = 'post'
    template_name = 'news/post_delete.html'
    success_url = reverse_lazy('post_list')