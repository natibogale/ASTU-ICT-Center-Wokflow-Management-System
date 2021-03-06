# Generated by Django 3.2.4 on 2021-09-30 14:15

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('roleName', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name_plural': 'Roles',
            },
        ),
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('teamName', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name_plural': 'Teams',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=500, unique=True, verbose_name='Badge Number')),
                ('firstName', models.CharField(blank=True, max_length=500, verbose_name='First Name')),
                ('lastName', models.CharField(blank=True, max_length=500, verbose_name='Last Name')),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=100, verbose_name='Gender')),
                ('email', models.CharField(max_length=500, unique=True, verbose_name='Email')),
                ('phoneNumber', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message='Please enter your phonenumber in the format starting with: 09 or +251', regex='^\\+?1?\\d{10,15}$')], verbose_name='Phone Number')),
                ('directorate', models.CharField(blank=True, default='ICT Center', max_length=500, null=True, verbose_name='Directorate')),
                ('emergencyContactName', models.CharField(blank=True, max_length=500, verbose_name='Emergency Contact Name')),
                ('emergencyContactPhone', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message='Please enter your phonenumber in the format starting with: 09 or +251', regex='^\\+?1?\\d{10,15}$')], verbose_name='Emergency Contact Phone')),
                ('profilePicture', models.ImageField(default='Profile_Pictures/default.png', upload_to='Profile_Pictures/', verbose_name='Profile Picture')),
                ('lastEdit', models.DateTimeField(auto_now=True, verbose_name='Last Edit')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.roles', verbose_name='Role')),
                ('team', models.ForeignKey(default=1, max_length=500, on_delete=django.db.models.deletion.CASCADE, to='authentication.teams', verbose_name='Team')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
