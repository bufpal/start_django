from django.contrib import messages
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
            messages.success(request, 'Successfully replied to post..')
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
            post.user = request.user
            post.ip = request.META['REMOTE_ADDR']
            post.save()
            messages.success(request, 'New post created successfully')
            return redirect(post)
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {
        'form': form,
    })


def post_edit(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method=='POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.ip = request.META['REMOTE_ADDR']
            post.save()
            messages.success(request, 'Modfied Post')
            return redirect(post)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_new.html', {
        'form': form,
    })


def comment_list(request):
    qs = Comment.objects.all()
    post_qs = Post.objects.all()
    return render(request, 'blog/comment_list.html', {
        'comment_list': qs,
        'post_list': post_qs,
    })