# Generated by Django 3.1.3 on 2020-11-10 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seminar',
            name='seminar_date',
            field=models.TextField(),
        ),
    ]