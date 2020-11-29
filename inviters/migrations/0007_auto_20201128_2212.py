# Generated by Django 3.1.3 on 2020-11-28 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inviters', '0006_auto_20201128_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='company_name',
            field=models.CharField(max_length=400, unique=True),
        ),
        migrations.AlterField(
            model_name='inviter',
            name='phone_num',
            field=models.CharField(max_length=11, unique=True),
        ),
        migrations.AlterField(
            model_name='monthof',
            name='month_name',
            field=models.CharField(default='فروردین', max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='monthof',
            name='month_number',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='cardstype',
            unique_together={('card_name', 'card_price')},
        ),
        migrations.AlterUniqueTogether(
            name='code',
            unique_together={('code_num', 'code_prev_num')},
        ),
        migrations.AlterUniqueTogether(
            name='codeusage',
            unique_together={('code', 'year_of_use', 'monthof', 'inviter', 'company')},
        ),
        migrations.AlterUniqueTogether(
            name='dailyofftime',
            unique_together={('inviter', 'start_date', 'end_date', 'description')},
        ),
        migrations.AlterUniqueTogether(
            name='hourlyofftime',
            unique_together={('inviter', 'date', 'start_time', 'end_time', 'description')},
        ),
        migrations.AlterUniqueTogether(
            name='seminar',
            unique_together={('year', 'month', 'day', 'company', 'is_vebinar')},
        ),
    ]
