# Generated by Django 4.2.9 on 2024-01-21 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0005_alter_myinfo_birthday'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='knowledge',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
