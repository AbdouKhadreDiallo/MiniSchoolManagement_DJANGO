# Generated by Django 3.1 on 2021-01-15 21:41

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('campus', '0004_auto_20210115_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etudiant',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
    ]
