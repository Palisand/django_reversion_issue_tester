from django.db import models


class Foo(models.Model):
    thing = models.CharField(max_length=255)
    stuff = models.CharField(max_length=255)


class Bar(models.Model):
    thing = models.CharField(max_length=255)
    stuff = models.CharField(max_length=255)
