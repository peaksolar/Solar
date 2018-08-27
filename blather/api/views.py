from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .serializers import BucketlistSerializer
from .serializers import PaymentSerializer
from .models import Bucketlist
from blat.models import Payment
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

class CreateViewDetails(generics.RetrieveAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer


class CreatePaymentView(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def perform_create(self, serializer):
        serializer.save()

class PaymentDetailView(generics.RetrieveAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
