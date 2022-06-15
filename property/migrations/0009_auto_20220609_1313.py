# Generated by Django 2.2.24 on 2022-06-09 10:13

from phonenumbers import parse as phn_parse, format_number as phn_format, is_valid_number
from phonenumbers import PhoneNumberFormat
from django.db import migrations


def format_phone_number(apps, schema_editor):
    flats = apps.get_model('property', 'Flat')
    for flat in flats.objects.all().filter(owner_pure_phone=''):
        parsed_phone_number = phn_parse(flat.owners_phonenumber, "RU")
        if is_valid_number(parsed_phone_number):
            flat.owner_pure_phone = phn_format(parsed_phone_number, PhoneNumberFormat.E164)
        else:
            flat.owner_pure_phone = ''
        flat.save()


def move_backward(apps, schema_editor):
    flats = apps.get_model('property', 'Flat')
    flats.objects.all().update(owner_pure_phone='')


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_auto_20220609_1240'),
    ]

    operations = [
        migrations.RunPython(format_phone_number, move_backward),
    ]
