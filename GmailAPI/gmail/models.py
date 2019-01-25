from django.db import models

# Create your models here.
class Request(models.Model):
    request_url3 = models.CharField(max_length=500)
