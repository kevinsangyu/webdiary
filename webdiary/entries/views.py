from django.http import HttpResponse
from django.shortcuts import render


def entry_list(request):
    return render(request, 'entries/entry_list.html')

