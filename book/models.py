import django.db.models
from django.db import models


# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=10, name="书名")


class Person(models.Model):
    name = models.CharField(max_length=10, name="名字")
    gender = models.BooleanField(name="性别")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, name="关联的书目")
