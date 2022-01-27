from django.shortcuts import render
from cdjango.modulos import facade


def home(request):
    return render(request, 'base/home.html', {})
