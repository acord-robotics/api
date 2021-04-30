# from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

# Create your views here.
class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = Book

class BookDetail(generics.RetrieveUpdaeDestroy): # Get (CRUD)
    queryset = Book.objects.all()
    serializer_class = BookSerializer