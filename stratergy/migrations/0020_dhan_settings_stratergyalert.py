# Generated by Django 4.2.8 on 2024-03-12 14:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stratergy', '0019_remove_alert_flag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dhan_Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_id', models.CharField(default='', max_length=100)),
                ('access_token', models.CharField(default='', max_length=1000)),
                ('is_active', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Dhan Setting',
                'verbose_name_plural': 'Dhan Settings',
            },
        ),
        migrations.CreateModel(
            name='StratergyAlert',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('datetime', models.DateTimeField(auto_now_add=True, null=True)),
                ('stratergy', models.CharField(choices=[('Manual Input', 'Manual Input')], default='', max_length=50)),
                ('segment', models.PositiveIntegerField(default=0)),
                ('token', models.CharField(default='', max_length=50)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('buy_syntax', models.TextField()),
                ('sell_syntax', models.TextField()),
                ('high', models.PositiveIntegerField(default=0)),
                ('low', models.PositiveIntegerField(default=5000000000000)),
                ('target', models.PositiveIntegerField(default=0)),
                ('function', models.CharField(choices=[('Activated', 'Activated'), ('Deactivated', 'Deactivated')], default='', max_length=50)),
                ('symbol', models.CharField(default='-----', max_length=50)),
                ('symbol_name', models.CharField(default='-----', max_length=50)),
                ('ltp', models.PositiveIntegerField(default=0)),
                ('current_volume', models.PositiveIntegerField(default=5000000000000)),
                ('last_volume', models.PositiveIntegerField(default=5000000000000)),
                ('gap', models.IntegerField(default=0)),
                ('position_status', models.CharField(choices=[('EMPTY', 'EMPTY'), ('POSITION_OPEN', 'POSITION_OPEN'), ('SCALP_POSITION_OPEN', 'SCALP_POSITION_OPEN'), ('POSITION_CLOSED', 'POSITION_CLOSED'), ('SCALP_POSITION_CLOSED', 'SCALP_POSITION_CLOSED')], default='', max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Stratergy Alert',
                'verbose_name_plural': 'Stratergy Alerts',
            },
        ),
    ]
