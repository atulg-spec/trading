# Generated by Django 4.2.7 on 2024-03-14 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stratergy', '0021_remove_stratergyalert_current_volume_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='stratergy_settings',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
