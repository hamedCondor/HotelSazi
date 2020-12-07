# Generated by Django 3.1.3 on 2020-12-07 18:54

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_num', models.CharField(max_length=3)),
                ('code_prev_num', models.IntegerField(default='0912')),
                ('code_name', models.CharField(max_length=1)),
            ],
            options={
                'ordering': ['code_num'],
                'unique_together': {('code_num', 'code_prev_num')},
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=400, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Inviter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_of_hired', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_of_fired', models.DateTimeField(blank=True, null=True)),
                ('date_of_start_esurance', models.DateTimeField(blank=True, null=True)),
                ('date_of_end_esurance', models.DateTimeField(blank=True, null=True)),
                ('is_ensured', models.BooleanField(default=False)),
                ('is_fired', models.BooleanField(default=False)),
                ('phone_num', models.CharField(max_length=11, unique=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inviters.company')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MonthOf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month_number', models.IntegerField(unique=True)),
                ('month_name', models.CharField(default='فروردین', max_length=20, unique=True)),
            ],
            options={
                'ordering': ['month_number'],
            },
        ),
        migrations.CreateModel(
            name='Seminar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(default=1400)),
                ('day', models.IntegerField(default=15)),
                ('is_vebinar', models.BooleanField(default=False)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inviters.company')),
                ('month', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inviters.monthof')),
            ],
            options={
                'unique_together': {('year', 'month', 'day', 'company', 'is_vebinar')},
            },
        ),
        migrations.CreateModel(
            name='TahatorSells',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_of_sell', models.CharField(max_length=30)),
                ('extra_detail', models.TextField(blank=True, null=True)),
                ('inviter', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inviters.inviter')),
                ('seminar', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inviters.seminar')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
                ('amount', models.CharField(max_length=20)),
                ('description', models.TextField(null=True)),
                ('inviter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inviters.inviter')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Penalty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
                ('amount', models.CharField(max_length=20)),
                ('description', models.TextField(null=True)),
                ('inviter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inviters.inviter')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HotelSaziSells',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inviter', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inviters.inviter')),
                ('seminar', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inviters.seminar')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HourlyOffTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('description', models.TextField(blank=True, null=True)),
                ('inviter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inviters.inviter')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('inviter', 'date', 'start_time', 'end_time', 'description')},
            },
        ),
        migrations.CreateModel(
            name='DailyOffTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(default=datetime.date.today)),
                ('end_date', models.DateField()),
                ('description', models.TextField(blank=True, null=True)),
                ('inviter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inviters.inviter')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('inviter', 'start_date', 'end_date', 'description')},
            },
        ),
        migrations.CreateModel(
            name='CodeUsage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_of_use', models.IntegerField(default=1400)),
                ('code', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inviters.code')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inviters.company')),
                ('inviter', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inviters.inviter')),
                ('monthof', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inviters.monthof')),
            ],
            options={
                'unique_together': {('code', 'year_of_use', 'monthof', 'inviter', 'company')},
            },
        ),
    ]
