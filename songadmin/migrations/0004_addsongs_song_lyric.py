# Generated by Django 5.0.4 on 2024-05-15 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songadmin', '0003_delete_addsong'),
    ]

    operations = [
        migrations.AddField(
            model_name='addsongs',
            name='song_lyric',
            field=models.FileField(null=True, upload_to='lyrics'),
        ),
    ]