# Generated by Django 2.2.7 on 2021-04-06 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mini_fb', '0007_remove_statusmessage_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='statusmessage',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mini_fb.Profile'),
            preserve_default=False,
        ),
    ]