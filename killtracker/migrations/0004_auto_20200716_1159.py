# Generated by Django 2.2.13 on 2020-07-16 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('killtracker', '0003_auto_20200716_1042'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tracker',
            old_name='is_activated',
            new_name='is_enabled',
        ),
    ]