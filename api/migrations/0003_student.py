# Generated by Django 5.1.3 on 2024-12-05 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_programmer_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=30)),
                ('sex', models.CharField(max_length=1)),
                ('Numficha', models.PositiveIntegerField(default=True)),
                ('Formacion', models.BooleanField(default=True)),
                ('FechaFormacion', models.DateField()),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]