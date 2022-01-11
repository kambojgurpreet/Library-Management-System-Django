from rest_framework import serializers
from .models import Book, Author, Customer

class AuthorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'popularity']

class BookSerializers(serializers.ModelSerializer):
    author = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Book
        fields = ['id', 'name', 'title', 'author', 'rating', 'popularity', 'books_issued_out', 'inventory_available']
    
    def validate(self, data):
        if data['books_issued_out'] > data['inventory_available']:
            raise serializers.ValidationError(
            'Books not available')
        return data

class CustomerSerializers(serializers.ModelSerializer):
    books_issued = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Customer
        fields = ['id', 'name', 'address', 'phone_no', 'email', 'books_issued', 'favorite_author']