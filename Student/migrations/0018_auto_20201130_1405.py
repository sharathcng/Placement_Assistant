# Generated by Django 3.1.2 on 2020-11-30 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0017_auto_20201130_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academic_table',
            name='markscard',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]