from django.http import HttpResponse
from django.shortcuts import render

def mysum(request, numbers):
    # numbers = [int(num) for num in numbers.split("/")]
    # result = sum(map(int, numbers.split("/")))
    result = sum(map(lambda s: int(s or 0), numbers.split("/")))
    return HttpResponse(result)
