from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)


class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey(
        to=Author,
        on_delete=models.DO_NOTHING
    )