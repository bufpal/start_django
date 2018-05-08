from django.http import HttpResponse
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