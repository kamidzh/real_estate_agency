# Generated by Django 2.2.24 on 2025-04-26 17:00

from django.db import migrations
import phonenumbers


def get_pure_numbers(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        pure_phone_number = phonenumbers.parse(flat.owners_phonenumber, 'RU')
        if phonenumbers.is_valid_number(pure_phone_number):
            flat.owner_pure_phone = phonenumbers.format_number(pure_phone_number, phonenumbers.PhoneNumberFormat.E164)
        else:
            flat.owner_pure_phone = ''
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_auto_20250426_1343'),
    ]

    operations = [
        migrations.RunPython(get_pure_numbers)
    ]
