import os
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from .forms import PostForm
from .models import Post

def post_form(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            # 방법1)
            '''
            post = Post()
            post.title = form.cleaned_data['title']
            post.content = form.cleaned_data['content']
            post.save()
            '''

            # 방법2)
            """
            post = Post(title = form.cleaned_data['title'],
                        content = form.cleaned_data['content'])
            post.save()
            """

            # 방법3)
            '''
            Post.objects.create(title = form.cleaned_data['title'],
                                content = form.cleaned_data['content'])
            '''

            # 방법4)
            Post.objects.create(**form.cleaned_data)

            return redirect('dojo:post_list')
    else:
        form = PostForm()

    return render(request, 'dojo/post_form.html', {
        'form': form,
    })


def mysum(request, numbers):
    # numbers = [int(num) for num in numbers.split("/")]
    # result = sum(map(int, numbers.split("/")))
    result = sum(map(lambda s: int(s or 0), numbers.split("/")))
    return HttpResponse(result)


def hello(request, name, age):
    return HttpResponse("안녕하세요, {}, {}살 이시네요".format(name, age))


def post_list(request):
    return render(request, 'dojo/layout.html')


def post_list1(request):
    name = "Ben"
    return HttpResponse("""<h1>Hello {name} </h1>
<p> welcome to the your World""".format(name=name)
    )


def post_list2(request):
    name = {"name": "Ben"}
    response = render(request, "dojo/post_list2.html", name)
    return response


def post_list3(request):
    json_response = JsonResponse({
        "items": ["python", "django", "data", "algorithm"],
        "message": "road to python and django developer",
    }, json_dumps_params={"ensure_ascii": False})
    return json_response


def excel_download(request):
    filepath = os.path.join(settings.BASE_DIR, "hotfoot-software.xls")
    filename = os.path.basename(filepath)
    with open(filepath, "rb") as f:
        response = HttpResponse(f, content_type='application/vnd.ms-excel') # content_type(MIME type) default = text/html
        response['Content-disposition'] = 'attachment; filename="{}"'.format(filename)
        return response