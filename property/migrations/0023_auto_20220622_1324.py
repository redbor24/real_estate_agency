# Generated by Django 2.2.24 on 2022-06-22 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0022_auto_20220622_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='flat',
            field=models.ManyToManyField(db_index=True, related_name='owners', to='property.Flat', verbose_name='Квартира'),
        ),
    ]
