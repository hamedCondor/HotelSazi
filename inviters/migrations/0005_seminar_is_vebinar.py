# Generated by Django 3.1.3 on 2020-11-28 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inviters', '0004_remove_sells_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='seminar',
            name='is_vebinar',
            field=models.BooleanField(default=False),
        ),
    ]
