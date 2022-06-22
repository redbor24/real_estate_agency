# Generated by Django 2.2.24 on 2022-06-18 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0018_auto_20220618_1823'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compliant',
            name='user',
        ),
        migrations.AddField(
            model_name='compliant',
            name='owner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, related_name='owner_compliants', to='property.Owner', verbose_name='Автор'),
            preserve_default=False,
        ),
    ]
