from django.http import HttpResponse
from django.shortcuts import render


def login(request):
    # return HttpResponse('login')
    return render(request, 'users/login.html')


def register(request):
    # return HttpResponse('register')
    return render(request, 'users/register.html')

