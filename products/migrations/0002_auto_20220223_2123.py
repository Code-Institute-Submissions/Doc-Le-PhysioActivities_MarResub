# Generated by Django 3.2.9 on 2022-02-23 21:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='friendly_name',
        ),
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
    ]