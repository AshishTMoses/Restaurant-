# Generated by Django 4.2.5 on 2023-11-01 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0005_orderdb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdb',
            name='Tele',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
