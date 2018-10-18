from django_tables2 import RequestConfig
from . import models
from . import forms
from .models import Customer
from .models import Payment
from .models import profile
from .tables import PaymentTable
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm, ProfileEditForm, UserEditForm
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.models import User
from django.db.models import Sum
from django.contrib.auth.forms import (UserChangeForm, PasswordChangeForm)
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext


# Create your views here.

def home(request):
    table = PaymentTable(Payment.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'index.html', {'table': table})


@login_required
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

@login_required
def comments(request):
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
    return render(request, 'comments.html', args)

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
                return render(request, 'main.html', {'form': form})

    else:
        form = LoginForm()
        return render(request, 'main.html', {'form': form, 'title': 'Login'})


def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('dashboard')
            else:
                return HttpResponse('Disabled Account')
        else:
            return render(request, 'main.html')
    else:
        return render_to_response('login.html')


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)
        return render(request, 'main.html', {'form': form, 'title': 'Change Password'})


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
    request.session.flush()
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


def forgotpassword(request):
    return render(request, 'forgot-password.html', {'message': 'Hello World'})


def register(request):
    if request.method == 'POST':
        user_form = forms.UserRegistrationForm(request.POST)

        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile = profile.Objects.create(user=new_user)
            return render(request, 'register_done.html', {'new_user': new_user})
    else:
        user_form = forms.UserRegistrationForm()
    return render(request, 'register.html', {'user_form': user_form})


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,
                                       data=request.POST,
                                       files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'profile updated successfully')
        else:
            messages.error(request, 'Error updating your Profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'accountedit.html', {'user_form': user_form, 'profile_form': profile_form})
