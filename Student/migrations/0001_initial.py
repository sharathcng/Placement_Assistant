# Generated by Django 3.0.5 on 2020-10-22 12:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateOfBirth', models.DateField(default=django.utils.timezone.now)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], default='Male', max_length=10)),
                ('phoneNumber', models.IntegerField(max_length=10)),
                ('course', models.CharField(max_length=100)),
                ('semester', models.IntegerField(choices=[('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], default='5', max_length=2)),
                ('hobbies', models.CharField(max_length=500)),
                ('bloodGroup', models.CharField(choices=[('O+', 'O+'), ('A+', 'A+'), ('B+', 'B+'), ('AB+', 'AB+'), ('O-', 'O-'), ('A-', 'A-'), ('B-', 'B-'), ('AB-', 'AB-')], default=')+', max_length=10)),
                ('knownLanguages', models.CharField(max_length=100)),
                ('currentAddress', models.TextField()),
                ('permanentAddress', models.TextField()),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SSLC_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college', models.CharField(max_length=100)),
                ('university', models.CharField(max_length=100)),
                ('yearOfPass', models.IntegerField(max_length=4)),
                ('CGPA', models.DecimalField(decimal_places=2, max_digits=4)),
                ('markscard', models.ImageField(null=True, upload_to='sslc/')),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PUC_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college', models.CharField(max_length=100)),
                ('university', models.CharField(max_length=100)),
                ('yearOfPass', models.IntegerField(max_length=4)),
                ('CGPA', models.DecimalField(decimal_places=2, max_digits=4)),
                ('markscard', models.ImageField(null=True, upload_to='puc/')),
                ('username', models.OneToOneField(default='PES1201802650', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MCA_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college', models.CharField(max_length=100)),
                ('university', models.CharField(max_length=100)),
                ('yearOfPass', models.IntegerField(max_length=4)),
                ('CGPA', models.DecimalField(decimal_places=2, max_digits=4)),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Degree_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college', models.CharField(max_length=100)),
                ('university', models.CharField(max_length=100)),
                ('yearOfPass', models.IntegerField(max_length=4)),
                ('CGPA', models.DecimalField(decimal_places=2, max_digits=4)),
                ('markscard', models.ImageField(null=True, upload_to='degree/')),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
