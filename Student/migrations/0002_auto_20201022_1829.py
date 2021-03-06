# Generated by Django 3.0.5 on 2020-10-22 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='degree_table',
            name='yearOfPass',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='mca_table',
            name='yearOfPass',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='puc_table',
            name='yearOfPass',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='sslc_table',
            name='yearOfPass',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='student_profile',
            name='phoneNumber',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='student_profile',
            name='semester',
            field=models.IntegerField(choices=[('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], default='5'),
        ),
    ]
