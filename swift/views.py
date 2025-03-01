from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(requests):
    return render(requests, 'index.html')

def red(requests):
    return render(requests, 'red.html')

def numbers(request):
    return render(request, '1989.html')

