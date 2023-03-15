from django.db import models

from cities.models import City


class Route(models.Model):
    name = models.CharField(
        max_length=50, unique=True, verbose_name='Назва маршруту'
    )
    travel_times = models.PositiveSmallIntegerField(
        verbose_name='Загальний час у дорозі'
    )
    from_city = models.ForeignKey(
        City, on_delete=models.CASCADE,
        related_name='route_from_city_set',
        verbose_name='Звідки'
    )
    to_city = models.ForeignKey(
        'cities.City', on_delete=models.CASCADE,
        related_name='route_to_city_set',
        verbose_name='Куди'
    )
    trains = models.ManyToManyField(
        'trains.Train', verbose_name='Список поїздів'
    )

    def __str__(self):
        return f'Маршрут {self.name} з міста {self.from_city}'

    class Meta:
        verbose_name = 'Маршрут'
        verbose_name_plural = 'Маршрути'
        ordering = ['travel_times']
