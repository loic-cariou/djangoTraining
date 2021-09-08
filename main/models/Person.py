from django.contrib.auth.models import User
from django.db import models


class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField()
# class Person(User):
#     birth_date = models.DateField()
