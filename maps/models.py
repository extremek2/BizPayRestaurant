from django.db import models

class Store(models.Model):
    store_id = models.AutoField(primary_key=True)
    store_name = models.CharField(max_length=100)
    store_address = models.CharField(max_length=100)
    store_phone = models.CharField(max_length=100)
    store_email = models.CharField(max_length=100)
    store_website = models.CharField(max_length=100)
    stor_lat = models.FloatField()
    stor_lon = models.FloatField()

# Create your models here.
