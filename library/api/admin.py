from django.contrib import admin
from .models import Book, Author, Customer

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'popularity']

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'title', 'authors', 'rating', 'popularity', 'books_issued_out', 'inventory_available']

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'address', 'phone_no', 'email', 'all_books_issued', 'favorite_author']