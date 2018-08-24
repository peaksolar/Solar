from django.db import models
from django_countries.fields import CountryField

# Create your models here.

class Blat(models.Model):
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    via = models.URLField(blank=True)

    def total_likes(self):
        return self.like_set.count()

    def __unicode__(self):
        return self.text[:50]


class Like(models.Model):
    blat = models.ForeignKey('Blat', on_delete=models.CASCADE,)

class Supplier(models.Model):
    company_name = models.CharField(max_length=50)
    contact_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    country = CountryField()
    phone = models.CharField(max_length=50)
    website = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.company_name


class ProductCategory(models.Model):
    catergory_name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    Quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.catergory_name

class Product(models.Model):
    payGID = models.CharField(max_length=12, primary_key=True)
    catergory_name = models.ForeignKey('ProductCategory', on_delete=models.CASCADE, )
    supplier_name = models.ForeignKey('Supplier', on_delete=models.CASCADE, )
    buyPrice = models.FloatField()
    sellPrice = models.FloatField()
    productDescription = models.TextField(null=True)

    def __str__(self):
        return self.payGID


class PaymentPlan(models.Model):
    planName = models.CharField(max_length=30)

    def __str__(self):
        return self.planName


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    country = CountryField()
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    payGID = models.ForeignKey('Product', on_delete=models.CASCADE,)
    paymentPlan = models.ForeignKey('PaymentPlan', on_delete=models.CASCADE, null = True )

    def __str__(self):
        return u'%s %s' %(self.first_name, self.last_name)


TOKEN_STATE = (
    ('active','ACTIVE'),
    ('new', 'NEW'),
)



class Tokens(models.Model):
    tokenID = models.AutoField(primary_key=True)
    tokenNumber = models.CharField(max_length=15)
    payGID = models.ForeignKey('Product', on_delete=models.CASCADE, )
    validity = models.IntegerField(default=30)
    status = models.CharField(max_length=6, choices=TOKEN_STATE, default='new')

    def __str__(self):
        return self.tokenNumber

PAYMENT_TYPES = (
    ('cash','CASH'),
    ('mobileMoney', 'MOBILE MONEY'),
)
class Payment(models.Model):
    customerName = models.ForeignKey('Customer', on_delete=models.CASCADE, )
    paymentDate = models.DateTimeField(auto_now_add=True, blank=True)
    amount = models.FloatField()
    payGID = models.ForeignKey('Product', on_delete=models.CASCADE, )
    paymentType = models.CharField(max_length=20, choices=PAYMENT_TYPES, default='cash')

TOKEN_SEQUENCE = [
    ('Token1', 'Token 1'),
    ('Token2', 'Token 1'),
    ('Token3', 'Token 1'),
    ('Token4', 'Token 1'),
    ('Token5', 'Token 1'),
    ('Token6', 'Token 1'),
    ('Token1', 'Token 1'),
    ('Token1', 'Token 1'),
    ('Token1', 'Token 1'),
    ('Token1', 'Token 1'),
    ('Token1', 'Token 1'),
    ('Token1', 'Token 1'),
    ('Token1', 'Token 1'),
    ('Token1', 'Token 1'),
    ('Token1', 'Token 1'),
    ('Token1', 'Token 1'),
    ('Token1', 'Token 1'),
    ('Token1', 'Token 1'),
    ('Token1', 'Token 1'),
    ('Token1', 'Token 1'),
    ('Token1', 'Token 1'),
    ('Token1', 'Token 1'),
    ('Token1', 'Token 1'),
    ('Token1', 'Token 1'),
    ('Token1', 'Token 1'),
    ('Token1', 'Token 1'),
    ('Token1', 'Token 1'),
    ('Token1', 'Token 1'),
    ('Token1', 'Token 1'),
    ('Token1', 'Token 1'),
    ('Token1', 'Token 1'),
    ('Token1', 'Token 1'),
    ('Token1', 'Token 1'),
    ('Token1', 'Token 1'),
    ('Token1', 'Token 1'),
    ('Token1', 'Token 1'),
    ('Token1', 'Token 1'),
    ('Token1', 'Token 1'),
    ('Token1', 'Token 1'),
    ('Token1', 'Token 1'),

]