from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    return HttpResponse("stores here, api's here, go there")
