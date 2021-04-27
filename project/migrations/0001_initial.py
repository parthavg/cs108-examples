# Generated by Django 2.2.7 on 2021-04-10 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.TextField(blank=True)),
                ('price', models.TextField(blank=True)),
                ('poster_image_url', models.URLField(blank=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True)),
                ('email_id', models.TextField(blank=True)),
                ('profile_image_url', models.URLField(blank=True)),
                ('mobile_number', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(blank=True)),
                ('time_stamp', models.TextField(blank=True)),
            ],
        ),
    ]
