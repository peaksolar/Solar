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
from django.db import connection
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.models import User
from django.db.models import Sum


# Create your views here.

def home(request):
    table = PaymentTable(Payment.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'index.html', {'table': table})


def profile(request):
    user = request.user
    customer = Customer.objects.get(username=user)
    customerpayments = Payment.objects.filter(username=user).order_by('-paymentDate')
    noOfpayments = Payment.objects.filter(username=user).count()
    amounts = Payment.objects.filter(username=user).values_list('amount', flat=True)
    total = sum(amounts)
    totaltokens = Payment.objects.filter(username=user).count()
    productPrice = models.Product.objects.get(payGID=customer.payGID)
    args = {'customer': customer, 'noOfpayments': noOfpayments,
            'total': total, 'totaltokens': totaltokens, 'productPrice': productPrice}
    return render(request, 'account.html', args)


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
        return render(request, 'main.html', {'form': form})


def customer_sql(self):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Customer WHERE first_name = %s", [self.first_name])
        row = cursor.fetchone()
    return row


@login_required
def dashboard(request):
    user = request.user
    customer = Customer.objects.get(username=user)
    customerpayments = Payment.objects.filter(username=user).order_by('-paymentDate')
    table = PaymentTable(customerpayments)
    noOfpayments = Payment.objects.filter(username=user).count()
    amounts = Payment.objects.filter(username=user).values_list('amount', flat=True)
    total = sum(amounts)
    totaltokens = Payment.objects.filter(username=user).count()
    productPrice = models.Product.objects.get(payGID=customer.payGID)
    RequestConfig(request).configure(table)
    args = {'table': table, 'customer': customer, 'noOfpayments': noOfpayments,
            'total': total, 'totaltokens': totaltokens, 'productPrice': productPrice}
    return render(request, 'index.html', args)


def logout(request):

    return render(request, 'logged_out.html', {'message': 'Hello World'})


@login_required
def billing(request):
    user = request.user
    customer = Customer.objects.get(username=user)
    customerpayments = Payment.objects.filter(username=user).order_by('-paymentDate')
    paginator = Paginator(customerpayments, 25)  # Show 25 contacts per page
    page = request.GET.get('page')
    payment_list = paginator.get_page(page)

    table = PaymentTable(customerpayments)
    noOfpayments = Payment.objects.filter(username=user).count()
    amounts = Payment.objects.filter(username=user).values_list('amount', flat=True)
    total = sum(amounts)
    totaltokens = Payment.objects.filter(username=user).count()
    productPrice = models.Product.objects.get(payGID=customer.payGID)
    AcoountBal = productPrice.sellPrice - total
    RequestConfig(request).configure(table)
    args = {'table': table, 'customer': customer, 'noOfpayments': noOfpayments,
            'total': total, 'totaltokens': totaltokens, 'productPrice': productPrice,
            'payment_list': payment_list, 'AcoountBal': AcoountBal}
    return render(request, 'billing.html', args)

