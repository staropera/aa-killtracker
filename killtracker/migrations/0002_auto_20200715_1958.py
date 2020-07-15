# Generated by Django 2.2.13 on 2020-07-15 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('killtracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='killmail',
            name='time',
            field=models.DateTimeField(blank=True, db_index=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='trackerkillmail',
            name='attackers_count',
            field=models.PositiveIntegerField(db_index=True, default=None, help_text='Calculated number of attackers', null=True),
        ),
        migrations.AlterField(
            model_name='trackerkillmail',
            name='date_sent',
            field=models.DateTimeField(db_index=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='trackerkillmail',
            name='distance',
            field=models.FloatField(db_index=True, default=None, help_text='Calculated distance from origin in lightyears', null=True),
        ),
        migrations.AlterField(
            model_name='trackerkillmail',
            name='is_high_sec',
            field=models.BooleanField(db_index=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='trackerkillmail',
            name='is_low_sec',
            field=models.BooleanField(db_index=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='trackerkillmail',
            name='is_matching',
            field=models.BooleanField(db_index=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='trackerkillmail',
            name='is_null_sec',
            field=models.BooleanField(db_index=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='trackerkillmail',
            name='is_w_space',
            field=models.BooleanField(db_index=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='trackerkillmail',
            name='jumps',
            field=models.PositiveIntegerField(db_index=True, default=None, help_text='Calculated number of jumps from origin', null=True),
        ),
    ]