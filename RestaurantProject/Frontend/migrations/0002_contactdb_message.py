# Generated by Django 4.2.5 on 2023-10-11 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactdb',
            name='Message',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
