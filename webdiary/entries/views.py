from django.http import HttpResponse
from django.shortcuts import render
from .models import Entry


def entry_list(request):
    entries = Entry.objects.all().order_by('date_created')
    return render(request, 'entries/entry_list.html', {'entries': entries})

