from django.db import models


class Address(models.Model):
    street = models.CharField(max_length=200, null=False, blank=False)
    city = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return "{} / {}".format(
            self.street or "? no street ?", self.city or "? no city ?"
        )
