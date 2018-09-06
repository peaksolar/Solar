import django_tables2 as tables
from .models import Payment


class PaymentTable(tables.Table):
    class Meta:
        model = Payment
        exclude = ('id', 'customerName', 'username', 'payGID',)
        template_name = 'django_tables2/bootstrap.html'
