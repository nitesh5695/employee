from django.shortcuts import render
from django.http import HttpResponse

def homeview(request):
    return HttpResponse("this is the home view")
