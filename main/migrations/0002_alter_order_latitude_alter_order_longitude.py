# Generated by Django 5.0.1 on 2024-01-30 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='latitude',
            field=models.CharField(max_length=50, verbose_name='Широта'),
        ),
        migrations.AlterField(
            model_name='order',
            name='longitude',
            field=models.CharField(max_length=50, verbose_name='Долгота'),
        ),
    ]
