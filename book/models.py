from django.db import models


# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField()
    detail = models.CharField(max_length=100)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
