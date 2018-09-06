from django_tables2 import RequestConfig
from . import models
from .models import Customer
from .models import Payment
from .tables import PaymentTable
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    table = PaymentTable(Payment.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'index.html', {'table': table})


def profile(request):
    return render(request, 'profile.html', {'message': 'Hello World'})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('dashboard')
                else:
                    return HttpResponse('Disabled Account')
            else:
                return HttpResponse('Invalid Login')
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})


@login_required
def dashboard(request):
    table = PaymentTable(Payment.objects.all())
    customer = Customer.objects.all()
    RequestConfig(request).configure(table)
    args = {'table': table, 'customer': customer}
    return render(request, 'index.html', args)


def logout(request):
    return render(request, 'logged_out.html', {'message': 'Hello World'})
