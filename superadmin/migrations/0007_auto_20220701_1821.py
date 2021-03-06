# Generated by Django 2.2.6 on 2022-07-01 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superadmin', '0006_auto_20220701_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='close_time',
            field=models.TimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='open_time',
            field=models.TimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='pincode',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='site_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
