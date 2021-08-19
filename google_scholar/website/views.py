from django.shortcuts import render
from django.http.request import HttpRequest
from .models import Organisation


def index(request: HttpRequest):
    # print(Organisation.objects.all())
    return render(request, 'website/base.html')
