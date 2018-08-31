from django.shortcuts import render
from .models import Payment
from django_tables2 import RequestConfig
from .models import Payment
from .tables import PaymentTable

# Create your views here.

def home(request):
    table = PaymentTable(Payment.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'index.html', {'table': table})

def profile(request):
    return render(request, 'profile.html', {'message': 'Hello World'})