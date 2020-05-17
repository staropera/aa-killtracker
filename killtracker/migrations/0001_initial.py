# Generated by Django 2.2.12 on 2020-05-17 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='General',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'permissions': (('basic_access', 'Can access this app'),),
                'managed': False,
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='EveEntity',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('alliance', 'alliance'), ('character', 'character'), ('constellation', 'constellation'), ('corporation', 'corporation'), ('faction', 'faction'), ('inventory_type', 'inventory_type'), ('region', 'region'), ('solar_system', 'solar_system'), ('station', 'station')], max_length=16)),
                ('timestamp', models.DateTimeField(auto_now=True, db_index=True)),
            ],
        ),
        migrations.CreateModel(
            name='Killmail',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('time', models.DateTimeField(blank=True, default=None, null=True)),
                ('solar_system_id', models.PositiveIntegerField(blank=True, default=None, null=True)),
                ('is_processed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='KillmailPosition',
            fields=[
                ('killmail', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='position', serialize=False, to='killtracker.Killmail')),
                ('x', models.FloatField(blank=True, default=None, null=True)),
                ('y', models.FloatField(blank=True, default=None, null=True)),
                ('z', models.FloatField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='KillmailVictim',
            fields=[
                ('character_id', models.PositiveIntegerField(blank=True, default=None, null=True)),
                ('corporation_id', models.PositiveIntegerField(blank=True, default=None, null=True)),
                ('alliance_id', models.PositiveIntegerField(blank=True, default=None, null=True)),
                ('faction_id', models.PositiveIntegerField(blank=True, default=None, null=True)),
                ('ship_type_id', models.PositiveIntegerField(blank=True, default=None, null=True)),
                ('killmail', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='victim', serialize=False, to='killtracker.Killmail')),
                ('damage_taken', models.BigIntegerField(blank=True, default=None, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='KillmailZkb',
            fields=[
                ('killmail', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='zkb', serialize=False, to='killtracker.Killmail')),
                ('location_id', models.PositiveIntegerField(blank=True, default=None, null=True)),
                ('hash', models.CharField(blank=True, default='', max_length=64)),
                ('fitted_value', models.FloatField(blank=True, default=None, null=True)),
                ('total_value', models.FloatField(blank=True, default=None, null=True)),
                ('points', models.PositiveIntegerField(blank=True, default=None, null=True)),
                ('is_npc', models.BooleanField(blank=True, default=None, null=True)),
                ('is_solo', models.BooleanField(blank=True, default=None, null=True)),
                ('is_awox', models.BooleanField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='KillmailAttacker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character_id', models.PositiveIntegerField(blank=True, default=None, null=True)),
                ('corporation_id', models.PositiveIntegerField(blank=True, default=None, null=True)),
                ('alliance_id', models.PositiveIntegerField(blank=True, default=None, null=True)),
                ('faction_id', models.PositiveIntegerField(blank=True, default=None, null=True)),
                ('ship_type_id', models.PositiveIntegerField(blank=True, default=None, null=True)),
                ('damage_done', models.BigIntegerField(blank=True, default=None, null=True)),
                ('is_final_blow', models.BooleanField(blank=True, default=None, null=True)),
                ('security_status', models.FloatField(blank=True, default=None, null=True)),
                ('weapon_type_id', models.PositiveIntegerField(blank=True, default=None, null=True)),
                ('killmail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attackers', to='killtracker.Killmail')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
