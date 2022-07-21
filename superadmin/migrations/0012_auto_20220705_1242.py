# Generated by Django 2.2.6 on 2022-07-05 07:12

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superadmin', '0011_background'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeaderBackground',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', colorfield.fields.ColorField(default='#FFFFFFFF', image_field=None, max_length=18, samples=None)),
            ],
            options={
                'db_table': 'headerbackground',
            },
        ),
        migrations.RenameModel(
            old_name='Background',
            new_name='FooterBackground',
        ),
        migrations.AlterModelTable(
            name='footerbackground',
            table='footerbackground',
        ),
    ]
