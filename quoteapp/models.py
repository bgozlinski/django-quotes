from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    birth_date = models.DateField()
    birth_place = models.CharField(max_length=25)
    description = models.TextField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Quote(models.Model):
    quote_text = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
