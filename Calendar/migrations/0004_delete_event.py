# Generated by Django 3.1.2 on 2020-12-01 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Calendar', '0003_event'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Event',
        ),
    ]