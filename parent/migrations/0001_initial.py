# Generated by Django 2.2.6 on 2022-07-01 06:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('prof_image', models.FileField(default='', upload_to='parent/profile_img/')),
                ('father_name', models.CharField(default='', max_length=100)),
                ('mother_name', models.CharField(default='', max_length=100)),
                ('occupation', models.CharField(choices=[(None, 'Select Occupation'), ('Managers', 'Managers'), ('Professional', 'Professional'), ('Technicians and associate professionals.', 'Technicians and associate professionals.'), ('Clerical support workers.', 'Clerical support workers.'), ('Service and sales workers.', 'Service and sales workers.'), ('Skilled agricultural, forestry and fishery workers.', 'Skilled agricultural, forestry and fishery workers.'), ('Plant and machine operators, and assemblers.', 'Plant and machine operators, and assemblers.'), ('Government and Public Administration.', 'Government and Public Administration.'), ('Agriculture, Food and Natural Resources. Architecture and Construction', 'Agriculture, Food and Natural Resources. Architecture and Construction'), ('Business and financial operations: Cost analyst', 'Business and financial operations: Cost analyst'), ('Law: Paralegal.', 'Law: Paralegal.'), ('Hospitality and Tourism', 'Hospitality and Tourism'), ('Manufacturing', 'Manufacturing')], default='', max_length=300)),
                ('blood_group', models.CharField(choices=[('None', 'Select Blood Group'), ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-')], default='', max_length=5)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='', max_length=50)),
                ('dob', models.DateTimeField(blank=True, null=True)),
                ('mobile', models.CharField(default='', max_length=13)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'parent',
            },
        ),
    ]
