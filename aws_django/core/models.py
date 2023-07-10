from django.db import models


# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=50)
    cover = models.ImageField()
