from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'shop/index.html')

def about(request):
    return HttpResponse("About")
def contact(request):
    return HttpResponse("About")
def tracker(request):
    return HttpResponse("About")
def search(request):
    return HttpResponse("About")
def productView(request):
    return HttpResponse("About")
def checkout(request):
    return HttpResponse("About")
# pswd:123456