# Generated by Django 2.2.7 on 2021-04-07 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mini_fb', '0009_profile_profile_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='statusmessage',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
