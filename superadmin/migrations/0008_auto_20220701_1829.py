# Generated by Django 2.2.6 on 2022-07-01 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superadmin', '0007_auto_20220701_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='close_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='address',
            name='open_time',
            field=models.TimeField(),
        ),
    ]
