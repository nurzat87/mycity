# Generated by Django 3.2.6 on 2021-08-11 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposal',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='proposal'),
        ),
    ]
