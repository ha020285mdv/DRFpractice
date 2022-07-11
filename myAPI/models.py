from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Writer(models.Model):
    name = models.CharField(max_length=200)
    age = models.SmallIntegerField(validators=[MaxValueValidator(120), MinValueValidator(10)])

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=300)
    writer = models.ForeignKey(Writer, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return f'"{self.title}" by {self.writer}'
