import os
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from .forms import PostForm
from .models import Post


class DetailView(object):
    '이전 FBV를 CBV버전으로 컨셉만 간단히 구현. 같은 동작을 수행'
    def __init__(self, model):
        self.model = model

    def get_object(self, *args, **kwargs):
        return get_object_or_404(self.model, id=kwargs['id'])

    def get_template_name(self):
        return '{}/{}_detail.html'.format(self.model._meta.app_label, self.model._meta.model_name)

    def dispatch(self, request, *args, **kwargs):
        return render(request, self.get_template_name(), {
        self.model._meta.model_name: self.get_object(*args, **kwargs),
        })

    @classmethod
    def as_view(cls, model):
        def view(request, *args, **kwargs):
            self = cls(model)
            return self.dispatch(request, *args, **kwargs)
        return view


post_detail = DetailView.as_view(Post)


def post_new(request):
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
            '''
            Post.objects.create(**form.cleaned_data)
            '''
            post = form.save(commit=False)
            post.ip = request.META['REMOTE_ADDR']
            post.save()
            return redirect('dojo:post_list')
    else:
        form = PostForm()

    return render(request, 'dojo/post_new.html', {
        'form': form,
    })


def post_edit(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.ip = request.META['REMOTE_ADDR']
            post.save()
            return redirect('dojo:post_list')
    else:
        form = PostForm(instance=post)
    
    return render(request, 'dojo/post_new.html', {
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