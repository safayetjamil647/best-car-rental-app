# Generated by Django 4.2.2 on 2023-06-27 06:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_destination', models.CharField(max_length=50)),
                ('to_destination', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=50)),
                ('pick_up_date', models.DateField()),
                ('pick_up_time', models.DateField()),
                ('end_time', models.DateField()),
                ('ordered_at', models.DateField(auto_now=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('deleted_at', models.DateField(auto_now=True)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.car')),
            ],
        ),
    ]
