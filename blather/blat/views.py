from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'blat/home.html', {'message': 'Hello World'})