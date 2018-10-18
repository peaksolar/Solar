from django.contrib import admin
from blat.models import Blat
from .models import Product
from .models import Customer
from .models import Tokens
from .models import Payment
from .models import PaymentPlan
from .models import ProductCategory
from .models import Supplier
from .models import profile
from api.models import Bucketlist

# Register your models here.
class BlatAdmin(admin.ModelAdmin):
    list_display = ('text', 'created_on', 'total_likes')
    list_filter = ['created_on']
    search_fields = ['text']

class Products(admin.ModelAdmin):
    list_display = ('payGID', 'catergory_name', 'supplier_name', 'buyPrice', 'sellPrice', 'productDescription')
    list_filter = ['supplier_name']
    search_fields = ['payGID']

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'city', 'phone', 'payGID', 'country', 'username', 'paymentPlan')
    list_filter = ['city']
    search_fields = ['first_name']

class TokenAdmin(admin.ModelAdmin):
    list_display = ('sequency', 'tokenID', 'tokenNumber', 'payGID', 'validity', 'status')
    list_filter = ['payGID']
    search_fields = ['payGID']

class CustomerPayments(admin.ModelAdmin):
    list_display = ('customerName', 'payGID', 'paymentDate', 'amount', 'paymentType', 'activation_token', 'username')
    list_filter = ['payGID']
    search_fields = ['customerName']

class PayPlan(admin.ModelAdmin):
    list_display = ['planName']

class Suppliers(admin.ModelAdmin):
    list_display = ('company_name', 'contact_name', 'address', 'country', 'phone', 'website', 'email')
    list_filter = ['country']
    search_fields = ['company_name']


class ProductCatergories(admin.ModelAdmin):
    list_display = ('catergory_name', 'description', 'Quantity')

class BucketListing(admin.ModelAdmin):
    list_display = ('name', 'date_created', 'date_modified', 'owner')

class profileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo']

#admin.site.register(Blat, BlatAdmin)
admin.site.register(Supplier, Suppliers)
admin.site.register(ProductCategory, ProductCatergories)
admin.site.register(Product, Products)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Tokens, TokenAdmin)
admin.site.register(PaymentPlan, PayPlan)
admin.site.register(Payment, CustomerPayments)
admin.site.register(Bucketlist, BucketListing)
admin.site.register(profile, profileAdmin)