from django.shortcuts import render
from django.http.request import HttpRequest
from .models import Organisation


# Create your views here.
def index(request: HttpRequest):
    # print(Organisation.objects.all())
    print(Organisation.objects.first())
    return None
