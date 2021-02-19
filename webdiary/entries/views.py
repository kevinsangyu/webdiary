from django.http import HttpResponse
from django.shortcuts import render
from .models import Entry


def entry_list(request):
    entries = Entry.objects.all().order_by('date_created')
    return render(request, 'entries/entry_list.html', {'entries': entries})


def entry_detail(request, slug):
    entry = Entry.objects.get(slug=slug)
    return render(request, 'entries/entry_detail.html', {'entry': entry})
    # return HttpResponse(slug)
