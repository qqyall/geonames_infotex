# Generated by Django 3.2 on 2024-05-13 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0006_auto_20240513_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geoname',
            name='country_code',
            field=models.CharField(blank=True, max_length=10, verbose_name='country_code'),
        ),
        migrations.AlterField(
            model_name='geoname',
            name='feature_class',
            field=models.CharField(blank=True, max_length=10, verbose_name='feature_class'),
        ),
    ]
