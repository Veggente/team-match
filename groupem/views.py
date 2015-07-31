from django.shortcuts import render

def index(request):
    return render(request, 'groupem/index.html')

def signup(request):
    return render(request, 'groupem/signup.html')
