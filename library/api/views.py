from .models import Book, Author, Customer
from .serializers import BookSerializers, AuthorSerializers, CustomerSerializers
from rest_framework import viewsets
import logging
logger = logging.getLogger('django')

class AuthorReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializers

class BookModelViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializers

class CustomerReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializers