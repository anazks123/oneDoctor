# Generated by Django 3.2.8 on 2022-05-20 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor_consultation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Patiant_name', models.CharField(max_length=200)),
                ('Patiant_disease', models.CharField(max_length=200)),
                ('Doctor_name', models.CharField(max_length=200)),
                ('appoiment_time', models.TimeField()),
                ('appointment_date', models.DateField()),
            ],
        ),
    ]
