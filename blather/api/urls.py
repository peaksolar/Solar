from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView
from .views import CreatePaymentView

urlpatterns = {
    url(r'^bucketlists/$', CreateView.as_view(), name="create"),
    url(r'^payments/$', CreatePaymentView.as_view(), name="pay"),
}

urlpatterns = format_suffix_patterns(urlpatterns)