from django.db import models

class Container(models.Model):
    name=models.TextField()
    date=models.DateField()
