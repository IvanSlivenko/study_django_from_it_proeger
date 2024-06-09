from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h4>Test work</h4>")

def about(request):
    return HttpResponse("<h4>test about</h4>")

def contacts(request):
    return HttpResponse("<h4>test contacts</h4>")
