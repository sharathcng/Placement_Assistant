# Generated by Django 3.0.2 on 2020-10-24 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Head', '0002_auto_20201024_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='Job_Description',
            field=models.TextField(),
        ),
    ]