from django.db import models

class Pages(models.Model):
    title= models.CharField(max_length=50 )
    description = models.TextField(blank=True, null=True)
    price= models.DecimalField(max_digits=20, decimal_places=2)
    summary= models.TextField(max_length=1000)
    featured = models.BooleanField(default=True)
# Create your models here.
