from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Entry
from django.contrib.auth.decorators import login_required
from . import forms
from django.contrib.auth.models import User


@login_required(login_url='/users/login/')
def entry_list(request):
    entries = Entry.objects.all().filter(author=request.user)
    return render(request, 'entries/entry_list.html', {'entries': entries})


@login_required(login_url='/users/login/')
def entry_detail(request, slug):
    entry = Entry.objects.get(slug=slug)
    return render(request, 'entries/entry_detail.html', {'entry': entry})
    # return HttpResponse(slug)


@login_required(login_url='/users/login/')
def new_entry(request):
    if request.method == "POST":
        form = forms.CreateEntry(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('list')
    else:
        form = forms.CreateEntry()
    return render(request, 'entries/new_entry.html', {'form': form})
