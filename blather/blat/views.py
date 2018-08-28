from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html', {'message': 'Hello World'})

def profile(request):
    return render(request, 'profile.html', {'message': 'Hello World'})