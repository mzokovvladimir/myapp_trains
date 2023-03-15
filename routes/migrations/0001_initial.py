from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('trains', '0002_auto_20201206_1351'),
        ('cities', '0003_auto_20201206_1344'),
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Назва маршруту')),
                ('travel_times', models.PositiveSmallIntegerField(verbose_name='Загальний час у дорозі')),
                ('from_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='route_from_city_set', to='cities.city', verbose_name='Звідки')),
                ('to_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='route_to_city_set', to='cities.city', verbose_name='Куди')),
                ('trains', models.ManyToManyField(to='trains.Train', verbose_name='Список поїздів')),
            ],
            options={
                'verbose_name': 'Маршрут',
                'verbose_name_plural': 'Маршрути',
                'ordering': ['travel_times'],
            },
        ),
    ]
