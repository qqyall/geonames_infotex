# Generated by Django 3.2 on 2024-05-13 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0005_auto_20240513_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geoname',
            name='alternatenames',
            field=models.CharField(blank=True, max_length=10000, verbose_name='Альтернативные названия'),
        ),
        migrations.AlterField(
            model_name='geoname',
            name='asciiname',
            field=models.CharField(blank=True, max_length=200, verbose_name='Hазвание(ascii)'),
        ),
        migrations.AlterField(
            model_name='geoname',
            name='modification_date',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='geoname',
            name='name',
            field=models.CharField(blank=True, max_length=200, verbose_name='Hазвание'),
        ),
        migrations.AlterField(
            model_name='geoname',
            name='population',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='geoname',
            name='timezone',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
