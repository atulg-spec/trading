# Generated by Django 4.2.8 on 2024-03-05 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stratergy', '0018_alert_flag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alert',
            name='flag',
        ),
    ]
