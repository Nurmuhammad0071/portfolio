# Generated by Django 4.2.9 on 2024-01-21 17:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='project_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
