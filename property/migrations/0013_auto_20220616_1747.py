# Generated by Django 2.2.24 on 2022-06-16 14:47

from django.db import migrations


def load_flat_owners(apps, schema_editor):
    Owner = apps.get_model('property', 'Owner')
    Flat = apps.get_model('property', 'Flat')

    flat_set = Flat.objects.all()
    for flt in flat_set.iterator():
        owner, created = Owner.objects.get_or_create(
            user=flt.owner,
            phone=flt.owners_phonenumber,
            pure_phone=flt.owner_pure_phone
        )
        owner.save()
        owner.flat.add(flt.id)


def clear_flat_owners(apps, schema_editor):
    Owner = apps.get_model('property', 'Owner')
    Owner.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_auto_20220616_1745'),
    ]

    operations = [
        migrations.RunPython(load_flat_owners, clear_flat_owners),
    ]
