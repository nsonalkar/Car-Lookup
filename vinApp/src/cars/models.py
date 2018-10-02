from django.db import models
from django.dispatch import receiver
from import_export.signals import post_import, post_export

# Create your models here.
class Cars(models.Model):
    vin = models.CharField('Vin Number', max_length=30)
    make = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    modelYear = models.CharField('Model Year', max_length=30)
    engineCylinders = models.CharField('Engine Cylinders',max_length=30)
    transmissionStyle = models.CharField('Transmission Style', max_length=30)
    trim = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "Cars"

    def __unicode__(self):
        return self.vin


