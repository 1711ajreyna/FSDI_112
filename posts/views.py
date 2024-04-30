from view.generic import (
    ListView,
    CreateView,
    DetailView
)

class PostListView(ListView):
    template_name = 'post/list.html'
    model = Post

class PostDetailView(DetailView):
    template_name = 'post/detail.html'
    model = Post

class PostCreateView(CreateView):
    template_name = 'posts/new.html'
    model = Post
    fields = ['title', 'subtitle', 'body']
