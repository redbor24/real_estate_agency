# Generated by Django 2.2.24 on 2022-06-22 10:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0024_auto_20220622_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='like',
            field=models.ManyToManyField(null=True, related_name='flat_likes', to=settings.AUTH_USER_MODEL, verbose_name='Кто лайкнул'),
        ),
    ]
