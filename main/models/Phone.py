from django.db import models
from main.models.Person import Person



class Phone(models.Model):

    phone_type = models.CharField(max_length=200, null=False, blank=False)
    value = models.CharField(max_length=200, null=False, blank=False)
    person = models.ForeignKey(Person, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return "{} / {}".format(
            self.phone_type or "? no type ?", self.value or "? no value ?"
        )
