from django.db import models
from main.models.Person import Person
from django.utils.translation import ugettext_lazy as _

class Phone(models.Model):
    PHONE_TYPE_MOBILE = 'mobile'
    PHONE_TYPE_EMERGENCY = 'emergency'
    PHONE_TYPE_HOME = 'home'
    PHONE_TYPE_WORK = 'work'
    PHONE_TYPES = (
        (PHONE_TYPE_MOBILE, _("Mobile")),
        (PHONE_TYPE_EMERGENCY, _("Emergency")),
        (PHONE_TYPE_HOME, _("Home")),
        (PHONE_TYPE_WORK, _("Work")),
    )
    type = models.CharField(
        max_length=50,
        choices=PHONE_TYPES,
        default=PHONE_TYPE_MOBILE,
    )
    person = models.ForeignKey(
        Person, null=True, on_delete=models.SET_NULL, related_name="phones"
    )
    value = models.CharField(max_length=200, null=False, blank=False)
    def __str__(self):
        return "{} : {} / {}".format(
            self.person,
            self.get_type_display() or "? no type ?",
            self.value or "? no value ?"
        )