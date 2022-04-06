from django.contrib import admin

# Register your models here.
from book.models import Book, Person
admin.site.register(Book)
admin.site.register(Person)
