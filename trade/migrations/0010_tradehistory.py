# Generated by Django 4.2.5 on 2024-04-30 12:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trade', '0009_bot_order_quantity_bankex_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='tradeHistory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date_time', models.DateTimeField(null=True)),
                ('symbol', models.CharField(default='', max_length=100)),
                ('client_id', models.CharField(default='', max_length=100)),
                ('buy_avg', models.FloatField()),
                ('sell_avg', models.FloatField()),
                ('pnl', models.FloatField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Trade History',
                'verbose_name_plural': 'Trade History',
            },
        ),
    ]
