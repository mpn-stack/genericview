from django.shortcuts import render
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response

class ProductListCreate(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset=Product.objects.all()
    serializer_class = ProductSerializer


    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Product.objects.all()
        try:
            pk = self.kwargs['pk']
        except:
            pk=None
        if pk is not None:
            queryset = queryset.filter(pk=pk)
        return queryset