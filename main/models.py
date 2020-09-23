from django.db import models
from phone_field import PhoneField

class Application(models.Model):
    F_name = models.CharField(max_length = 50, blank=True, null=True)
    M_name = models.CharField(max_length = 50, blank=True, null=True)
    S_name = models.CharField(max_length = 50, blank=True, null=True)
    email = models.EmailField(max_length = 50, blank=True, null=True)
    phone_num = PhoneField(blank=True, help_text='Contact phone number')
    course = models.CharField(max_length = 150, blank=True, null=True)
    message = models.CharField(max_length = 1050, blank=True, null=True)

    def __str__(self):
        return f"My name is {self.S_name}"