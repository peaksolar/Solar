from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .serializers import BucketlistSerializer
from .serializers import PaymentSerializer
from .models import Bucketlist
from blat.models import Payment

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

class CreatePaymentView(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def perform_create(self, serializer):
        serializer.save()