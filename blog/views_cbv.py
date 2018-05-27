from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from .models import Post


class PostListView(ListView):
    model = Post
    queryset = Post.objects.all().select_related('user')
    paginate_by = 10

post_list = PostListView.as_view()

post_detail = DetailView.as_view(model=Post, pk_url_kwarg='id')

post_new = CreateView.as_view(model=Post, fields='__all__')

post_edit = UpdateView.as_view(model=Post, fields='__all__')

post_delete = DeleteView.as_view(model=Post, success_url=reverse_lazy('blog:post_list'))
