# Generated by Django 4.2.7 on 2024-03-18 09:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stratergy', '0023_executed_stratergy_symbol_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='executed_stratergy',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 18, 9, 10, 32, 774986, tzinfo=datetime.timezone.utc), primary_key=True, serialize=False),
        ),
    ]
