from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cities', '0003_auto_20201206_1344'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Номер поїзда')),
                ('from_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cities.city',
                                                verbose_name='Звідки')),
            ],
        ),
        migrations.CreateModel(
            name='Train',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Номер поїзда')),
                ('travel_time', models.PositiveSmallIntegerField(verbose_name='Час у дорозі')),
                ('from_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                                related_name='from_city_set', to='cities.city',
                                                verbose_name='Звідки')),
                ('to_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_city_set',
                                              to='cities.city', verbose_name='Куди')),
            ],
            options={
                'verbose_name': 'Поїзд',
                'verbose_name_plural': 'Поїзди',
                'ordering': ['travel_time'],
            },
        ),
    ]
