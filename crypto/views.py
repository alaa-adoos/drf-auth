from django.shortcuts import render

from .models import Crypto
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import CryptoSerializer
from .permissions import OwnerOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly
class CryptoListCreateView(ListCreateAPIView):
    queryset=Crypto.objects.all()
    serializer_class=CryptoSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]

class CryptoDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Crypto.objects.all()
    serializer_class=CryptoSerializer
    permission_classes=[OwnerOnly]