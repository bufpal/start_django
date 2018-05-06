from django.shortcuts import render

def post_views(request):
    return render(request, 'blog/post_list.html')
