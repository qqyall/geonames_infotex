# Generated by Django 3.2 on 2024-05-13 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0004_auto_20240513_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geoname',
            name='admin1_code',
            field=models.CharField(blank=True, max_length=20, verbose_name='admin1_code'),
        ),
        migrations.AlterField(
            model_name='geoname',
            name='admin2_code',
            field=models.CharField(blank=True, max_length=80, verbose_name='admin2_code'),
        ),
        migrations.AlterField(
            model_name='geoname',
            name='admin3_code',
            field=models.CharField(blank=True, max_length=20, verbose_name='admin3_code'),
        ),
        migrations.AlterField(
            model_name='geoname',
            name='admin4_code',
            field=models.CharField(blank=True, max_length=20, verbose_name='admin4_code'),
        ),
        migrations.AlterField(
            model_name='geoname',
            name='cc2',
            field=models.CharField(blank=True, max_length=200, verbose_name='cc2'),
        ),
        migrations.AlterField(
            model_name='geoname',
            name='country_code',
            field=models.CharField(blank=True, max_length=2, verbose_name='country_code'),
        ),
        migrations.AlterField(
            model_name='geoname',
            name='elevation',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='geoname',
            name='feature_class',
            field=models.CharField(blank=True, max_length=1, verbose_name='feature_class'),
        ),
        migrations.AlterField(
            model_name='geoname',
            name='feature_code',
            field=models.CharField(blank=True, max_length=10, verbose_name='feature_code'),
        ),
    ]
