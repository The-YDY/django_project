# Generated by Django 4.0.5 on 2022-11-11 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='products/%Y/%m/%d')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('type', models.CharField(max_length=100)),
                ('make', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('first_registration', models.CharField(max_length=100)),
                ('mileage', models.IntegerField()),
                ('fuel', models.CharField(max_length=100)),
                ('engine_size', models.IntegerField()),
                ('power', models.IntegerField()),
                ('gearbox', models.CharField(max_length=100)),
                ('number_of_seats', models.IntegerField()),
                ('doors', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('vehicle_extras', models.TextField()),
                ('vehicle_description', models.TextField()),
                ('contact_name', models.CharField(max_length=200)),
                ('contact_phone', models.CharField(max_length=100)),
                ('contact_mobile_phone', models.CharField(max_length=100)),
                ('contact_email', models.EmailField(max_length=255)),
                ('available', models.BooleanField(default=True)),
                ('featured', models.BooleanField(default=False)),
            ],
        ),
    ]
