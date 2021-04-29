# Generated by Django 2.2.7 on 2021-04-27 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0010_profile_friends'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='fav_genre',
            field=models.CharField(choices=[('actions', 'Action'), ('dramas', 'Drama'), ('comedies', 'Comedy'), ('romance', 'Romance'), ('thrillers', 'Thriller')], default='actions', max_length=100),
            preserve_default=False,
        ),
    ]
