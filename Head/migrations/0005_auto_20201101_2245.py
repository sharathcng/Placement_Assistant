# Generated by Django 3.0.2 on 2020-11-01 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Head', '0004_auto_20201025_1455'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='criteria',
            name='Company_Name',
        ),
        migrations.RemoveField(
            model_name='test',
            name='Company_Name',
        ),
        migrations.DeleteModel(
            name='Company',
        ),
        migrations.DeleteModel(
            name='Criteria',
        ),
        migrations.DeleteModel(
            name='Test',
        ),
    ]