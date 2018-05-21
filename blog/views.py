from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from .forms import CommentForm, PostForm
from .models import Post, Comment


def post_list(request):
    qs = Post.objects.all()

    q = request.GET.get('q', '')
    if q:
        qs = Post.objects.filter(title__icontains=q)

    return render(request, 'blog/post_list.html', {
        'post_list': qs,
        'q': q,
    })


def post_detail(request, id):
    # try:
    #     post = Post.objects.get(id=id)
    # except Post.DoesNotExist:
    #     raise Http404

    post = get_object_or_404(Post, id=id)

    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post_id = id
            comment.save()
            return redirect(post)
    else:
        form = CommentForm()        

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'form': form,
    })


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = User.objects.get(id=1)
            post.ip = request.META['REMOTE_ADDR']
            post.save()
            return redirect('blog:post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_new.html', {
        'form': form,
    })


def post_edit(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method=='POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = User.objects.get(id=1)
            post.ip = request.META['REMOTE_ADDR']
            post.save()
            return redirect(post)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_new.html', {
        'form': form,
    })


# def post_comment(request, id):
#     if request.method == 'POST':
#         form = CommentForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('blog:post_list')
#     else:
#         form = CommentForm()
#     return render(request, 'blog/post_detail.html', {
#         'form': form
#     })