# Generated by Django 2.2.7 on 2021-04-27 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0009_auto_20210426_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='friends',
            field=models.ManyToManyField(related_name='_profile_friends_+', to='project.Profile'),
        ),
    ]
