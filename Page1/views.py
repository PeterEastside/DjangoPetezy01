from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def HomePage(request):
    return HttpResponse("<h1>HI GOD JADE<h1>")