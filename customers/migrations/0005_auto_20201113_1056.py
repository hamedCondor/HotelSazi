# Generated by Django 3.1.3 on 2020-11-13 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0004_auto_20201113_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invited',
            name='phone_num',
            field=models.CharField(max_length=11),
        ),
    ]
