# Generated by Django 2.2.7 on 2021-04-27 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0014_auto_20210427_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poster',
            name='category',
            field=models.CharField(choices=[('vintage', 'Vintages'), ('modern', 'Moderns'), ('classic', 'Classics')], max_length=100),
        ),
    ]
