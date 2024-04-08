from django.db import models

# Create your models here.
class Train(models.Model):
    id=models.AutoField(primary_key=True)
    arrets=models.CharField(max_length=100)
    destination=models.CharField(max_length=100)
    depart=models.CharField(max_length=100)
    arrivee=models.CharField(max_length=105)