# Generated by Django 3.2.9 on 2021-11-16 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prestamos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libro', models.CharField(max_length=100)),
                ('alumno', models.CharField(max_length=60)),
                ('fecha_prestamo', models.DateField()),
                ('fecha_devolucion', models.DateField()),
            ],
        ),
    ]
