from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

def home_view(request: HttpRequest):
    return render(request, 'search/google.html')

def terms_view(request: HttpRequest):
    return render(request, 'search/terms.html')
