# Generated by Django 2.2.7 on 2021-04-10 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mini_fb', '0012_profile_friends'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='friends',
            field=models.ManyToManyField(related_name='_profile_friends_+', to='mini_fb.Profile'),
        ),
    ]