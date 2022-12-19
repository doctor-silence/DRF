from django.db import models
from phone_field import PhoneField

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    phone = PhoneField(blank=True, help_text='Contact phone number')

    def __str__(self):
        return self.first_name