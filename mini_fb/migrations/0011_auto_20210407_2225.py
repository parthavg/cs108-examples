# Generated by Django 2.2.7 on 2021-04-07 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mini_fb', '0010_statusmessage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statusmessage',
            name='time_stamp',
            field=models.TimeField(blank=True),
        ),
    ]