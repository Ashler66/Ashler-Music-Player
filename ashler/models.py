from django.db import models

# Create your models here.
class Lib(models.Model):
    song_id=models.IntegerField(null=True)