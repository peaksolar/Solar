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

TOKEN_SEQUENCE = {
    ('Token1', 'Token 1'),
    ('Token2', 'Token 2'),
    ('Token3', 'Token 3'),
    ('Token4', 'Token 4'),
    ('Token5', 'Token 5'),
    ('Token6', 'Token 6'),
    ('Token7', 'Token 7'),
    ('Token8', 'Token 8'),
    ('Token9', 'Token 9'),
    ('Token10', 'Token 10'),
    ('Token11', 'Token 11'),
    ('Token12', 'Token 12'),
    ('Token13', 'Token 13'),
    ('Token14', 'Token 14'),
    ('Token15', 'Token 15'),
    ('Token16', 'Token 16'),
    ('Token17', 'Token 17'),
    ('Token18', 'Token 18'),
    ('Token19', 'Token 19'),
    ('Token20', 'Token 20'),
    ('Token21', 'Token 21'),
    ('Token22', 'Token 22'),
    ('Token23', 'Token 23'),
    ('Token24', 'Token 24'),
    ('Token25', 'Token 25'),
    ('Token26', 'Token 26'),
    ('Token27', 'Token 27'),
    ('Token28', 'Token 28'),
    ('Token29', 'Token 29'),
    ('Token30', 'Token 30'),
    ('Token31', 'Token 31'),
    ('Token32', 'Token 32'),
    ('Token33', 'Token 33'),
    ('Token34', 'Token 34'),
    ('Token35', 'Token 35'),
    ('Token36', 'Token 36'),
    ('Token37', 'Token 37'),
    ('Token38', 'Token 38'),
    ('Token39', 'Token 39'),
    ('Token40', 'Token 40'),
    ('Token41', 'Token 41'),
    ('Token42', 'Token 42'),
    ('Token43', 'Token 43'),
    ('Token44', 'Token 44'),
    ('Token45', 'Token 45'),
    ('Token46', 'Token 46'),
    ('Token47', 'Token 47'),
    ('Token48', 'Token 48'),
    ('Unlock', 'Unlock'),

}

class Tokens(models.Model):
    tokenID = models.AutoField(primary_key=True)
    tokenNumber = models.CharField(max_length=15)
    payGID = models.ForeignKey('Product', on_delete=models.CASCADE, )
    validity = models.IntegerField(default=30)
    status = models.CharField(max_length=6, choices=TOKEN_STATE, default='new')
    sequency = models.CharField(max_length=20, choices=TOKEN_SEQUENCE, default='Token1')

    def __str__(self):
        return u'%s %s' % (self.sequency, self.tokenNumber)