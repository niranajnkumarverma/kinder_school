# Generated by Django 2.2.6 on 2022-07-01 06:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0001_initial'),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Security',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('prof_image', models.FileField(default='', upload_to='security/profile_img/')),
                ('father_name', models.CharField(default='', max_length=100)),
                ('mother_name', models.CharField(default='', max_length=100)),
                ('father_occupation', models.CharField(choices=[(None, 'Select Occupation'), ('Managers', 'Managers'), ('Professional', 'Professional'), ('Technicians and associate professionals.', 'Technicians and associate professionals.'), ('Clerical support workers.', 'Clerical support workers.'), ('Service and sales workers.', 'Service and sales workers.'), ('Skilled agricultural, forestry and fishery workers.', 'Skilled agricultural, forestry and fishery workers.'), ('Plant and machine operators, and assemblers.', 'Plant and machine operators, and assemblers.'), ('Government and Public Administration.', 'Government and Public Administration.'), ('Agriculture, Food and Natural Resources. Architecture and Construction', 'Agriculture, Food and Natural Resources. Architecture and Construction'), ('Business and financial operations: Cost analyst', 'Business and financial operations: Cost analyst'), ('Law: Paralegal.', 'Law: Paralegal.'), ('Hospitality and Tourism', 'Hospitality and Tourism'), ('Manufacturing', 'Manufacturing')], default='', max_length=300)),
                ('dob', models.DateTimeField(blank=True, null=True)),
                ('blood_group', models.CharField(choices=[('None', 'Select Blood Group'), ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-')], default='A+', max_length=5)),
                ('religion', models.CharField(choices=[('Select Religion', 'Select religion'), ('Hindu', 'Hindu'), ('Islam', 'Islam'), ('Christian', 'Christian'), ('Buddish', 'Buddish'), ('Others', 'Others')], default='', max_length=15)),
                ('mobile', models.CharField(default='', max_length=10)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='', max_length=50)),
                ('address', models.TextField(default='', max_length=50)),
                ('pincode', models.CharField(default='', max_length=6)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('city', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='student.City')),
                ('country', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='student.Country')),
                ('state', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='student.State')),
            ],
            options={
                'db_table': 'security',
            },
        ),
    ]