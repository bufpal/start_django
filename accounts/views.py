from django.http import HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import render


def welcome_message(request):
    rendered = render_to_string('accounts/welcome_message.txt', {
        'name': 'Brandon',
        'date': '2018/5/14',
    })
    return HttpResponse(rendered)
