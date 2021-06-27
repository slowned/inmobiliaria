# Generated by Django 3.2.3 on 2021-06-26 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='home_type',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Casa'), (1, 'departamento'), (2, 'PH'), (3, 'Duplex')], default=0),
        ),
    ]