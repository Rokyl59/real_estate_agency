# Generated by Django 2.2.24 on 2024-05-05 07:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_link_flats_owners'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owner_pure_phone',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owners_phonenumber',
        ),
    ]