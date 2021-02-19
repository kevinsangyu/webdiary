from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def login(request):
    # return HttpResponse('login')
    return render(request, 'users/login.html')


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

