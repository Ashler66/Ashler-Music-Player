from django.db import models

class addsongs(models.Model):
    song_name=models.CharField(max_length=150)
    artist_name=models.CharField(max_length=150)
    song_link=models.FileField(upload_to="songs")
    song_image=models.ImageField(upload_to="images")
    song_lyric=models.FileField(upload_to="lyrics", null=True)

