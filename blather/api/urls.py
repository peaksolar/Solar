from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView
from .views import CreatePaymentView
from .views import PaymentDetailView
from .views import CreateViewDetails
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = {

    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^bucketlists/$', CreateView.as_view(), name="create"),
    url(r'^payments/$', CreatePaymentView.as_view(), name="pay"),
    url(r'^payments/(?P<pk>[0-9]+)/$', PaymentDetailView.as_view(), name="payment_details"),
    url(r'^bucketlists/(?P<pk>[0-9]+)/$', CreateViewDetails.as_view(), name="bucketlist_view"),
   # url(r'^users/$', UserView.as_view(), name="users"),
   # url(r'users/(?P<pk>[0-9]+)/$', UserDetailsView.as_view(), name="user_details"),
    url(r'^get-token/', obtain_auth_token),  # Add this line

}

urlpatterns = format_suffix_patterns(urlpatterns)