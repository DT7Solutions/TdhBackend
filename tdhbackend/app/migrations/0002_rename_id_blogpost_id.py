# Generated by Django 4.2.6 on 2023-10-16 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='Id',
            new_name='id',
        ),
    ]
