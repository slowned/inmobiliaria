# Generated by Django 3.2.1 on 2021-05-22 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('owners', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('available', models.BooleanField()),
                ('coordinates', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('services', models.CharField(choices=[], max_length=50)),
                ('tenant', models.CharField(max_length=100)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='properties', to='owners.owner')),
            ],
        ),
    ]
