from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Author(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    popularity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(100)])
    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    title = models.CharField(max_length=100)
    author = models.ManyToManyField(Author)
    rating = models.PositiveIntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(10)])
    popularity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(100)])
    books_issued_out = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    inventory_available = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    def __str__(self):
        return self.name

    def authors(self):
        return ', '.join([str(i.name) for i in self.author.all()])

class Customer(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    address = models.CharField(max_length=200, null=True, blank=True)
    phone_no = models.CharField(max_length=13, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    books_issued = models.ManyToManyField(Book)
    def __str__(self):
        return self.name

    def all_books_issued(self):
        return ', '.join([str(i.name) for i in self.books_issued.all()])

    def favorite_author(self):
        authors = {}
        authors_data = []
        for book in self.books_issued.all():
            for author in book.author.all():
                if author.id in authors:
                    authors[author.id] += 1
                else:
                    authors[author.id] = 1
                    authors_data.append(author)
        
        if authors.keys():
            fav_author_id = max(authors, key= lambda x: authors[x])
            for author in authors_data:
                if author.id == fav_author_id:
                    return author.name
        else:
            return None