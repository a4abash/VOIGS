from django.db import models
from django.contrib.auth.models import User


# models are created here
class Information(models.Model):
    name = models.CharField(help_text='andy sherpa', max_length=20)
    BikeNo = models.CharField(help_text='ba.2.pa.2255', max_length=20, unique=True)
    CitizenNo = models.CharField(max_length=20, help_text='05-02-71-00304', unique=True)
    LiscenseNo = models.CharField(max_length=20, help_text='06-539235', unique=True)
    BloodGroup = models.CharField(max_length=5, help_text='O+')

    def __str__(self):
        return self.name