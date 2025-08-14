from django.db import models

class Store(models.Model):
    store_id = models.AutoField(primary_key=True)
    store_name = models.CharField(max_length=100)
    store_address = models.CharField(max_length=100)
    store_phone = models.CharField(max_length=100)
    store_email = models.CharField(max_length=100)
    store_website = models.CharField(max_length=100)
    store_lat = models.FloatField()
    store_lon = models.FloatField()

# 참고 사항
# lat: y
# lon: x