from django.db import models


class Geoname(models.Model):
    """Класс населенного пункта"""

    geonameid = models.CharField(max_length=10)
    name = models.CharField(
        max_length=200,
        verbose_name='Hазвание',
        blank=True
    )
    asciiname = models.CharField(
        max_length=200,
        verbose_name='Hазвание(ascii)',
        blank=True
    )
    alternatenames = models.CharField(
        max_length=10000,
        verbose_name='Альтернативные названия',
        blank=True
    )
    latitude = models.CharField(
        max_length=10,
        blank=False
    )
    longitude = models.CharField(
        max_length=10,
        blank=False
    )
    feature_class = models.CharField(
        max_length=10,
        verbose_name='feature_class',
        blank=True
    )
    feature_code = models.CharField(
        max_length=10,
        verbose_name='feature_code',
        blank=True
    )
    country_code = models.CharField(
        max_length=10,
        verbose_name='country_code',
        blank=True
    )
    cc2 = models.CharField(
        max_length=200,
        verbose_name='cc2',
        blank=True
    )
    admin1_code = models.CharField(
        max_length=20,
        verbose_name='admin1_code',
        blank=True
    )
    admin2_code = models.CharField(
        max_length=80,
        verbose_name='admin2_code',
        blank=True
    )
    admin3_code = models.CharField(
        max_length=20,
        verbose_name='admin3_code',
        blank=True
    )
    admin4_code = models.CharField(
        max_length=20,
        verbose_name='admin4_code',
        blank=True
    )
    population = models.CharField(
        max_length=100,
        blank=True
    )
    elevation = models.CharField(
        max_length=100,
        blank=True
    )
    dem = models.CharField(
        max_length=100,
        blank=True
    )
    timezone = models.CharField(
        max_length=100,
        blank=True
    )
    modification_date = models.CharField(
        max_length=100,
        blank=True
    )
