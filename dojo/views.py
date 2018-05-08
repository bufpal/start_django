import os
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


def mysum(request, numbers):
    # numbers = [int(num) for num in numbers.split("/")]
    # result = sum(map(int, numbers.split("/")))
    result = sum(map(lambda s: int(s or 0), numbers.split("/")))
    return HttpResponse(result)


def hello(request, name, age):
    return HttpResponse("안녕하세요, {}, {}살 이시네요".format(name, age))


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