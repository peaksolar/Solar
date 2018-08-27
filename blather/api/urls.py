from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView
from .views import CreatePaymentView
from .views import PaymentDetailView
from .views import CreateViewDetails


urlpatterns = {
    url(r'^bucketlists/$', CreateView.as_view(), name="create"),
    url(r'^payments/$', CreatePaymentView.as_view(), name="pay"),
    url(r'^payments/(?P<pk>[0-9]+)/$', PaymentDetailView.as_view(), name="payment_details"),
    url(r'^bucketlists/(?P<pk>[0-9]+)/$', CreateViewDetails.as_view(), name="bucketlist_view"),
}

urlpatterns = format_suffix_patterns(urlpatterns)