# Generated by Django 3.2.8 on 2022-05-21 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorAdd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Doctor_name', models.CharField(max_length=200)),
                ('Doctor_spacial', models.CharField(max_length=200)),
                ('Doctor_Join_Date', models.DateField()),
            ],
        ),
    ]
