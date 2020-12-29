# Generated by Django 3.1.4 on 2020-12-29 01:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("eveonline", "0012_index_additions"),
        ("auth", "0012_alter_user_first_name_max_length"),
        ("eveuniverse", "0004_effect_longer_name"),
        ("killtracker", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="tracker",
            name="color",
            field=models.CharField(
                blank=True,
                default="",
                help_text="Optional color for embed on Discord - #000000 / black means no color selected",
                max_length=7,
            ),
        ),
        migrations.AddField(
            model_name="tracker",
            name="ping_groups",
            field=models.ManyToManyField(
                blank=True,
                default=None,
                help_text="Option to ping specific group members - ",
                related_name="_tracker_ping_groups_+",
                to="auth.Group",
                verbose_name="group pings",
            ),
        ),
        migrations.AddField(
            model_name="tracker",
            name="require_victim_ship_types",
            field=models.ManyToManyField(
                blank=True,
                default=None,
                help_text="Only include killmails where victim is flying one of these ship types",
                related_name="_tracker_require_victim_ship_types_+",
                to="eveuniverse.EveType",
            ),
        ),
        migrations.AlterField(
            model_name="tracker",
            name="exclude_attacker_alliances",
            field=models.ManyToManyField(
                blank=True,
                default=None,
                help_text="exclude killmails with attackers from one of these alliances",
                related_name="_tracker_exclude_attacker_alliances_+",
                to="eveonline.EveAllianceInfo",
            ),
        ),
        migrations.AlterField(
            model_name="tracker",
            name="exclude_attacker_corporations",
            field=models.ManyToManyField(
                blank=True,
                default=None,
                help_text="exclude killmails with attackers from one of these corporations",
                related_name="_tracker_exclude_attacker_corporations_+",
                to="eveonline.EveCorporationInfo",
            ),
        ),
        migrations.AlterField(
            model_name="tracker",
            name="origin_solar_system",
            field=models.ForeignKey(
                blank=True,
                default=None,
                help_text="Solar system to calculate distance and jumps from. When provided distance and jumps will be shown on killmail messages",
                null=True,
                on_delete=django.db.models.deletion.SET_DEFAULT,
                related_name="+",
                to="eveuniverse.evesolarsystem",
            ),
        ),
        migrations.AlterField(
            model_name="tracker",
            name="ping_type",
            field=models.CharField(
                choices=[("PN", "(none)"), ("PH", "@here"), ("PE", "@everybody")],
                default="PN",
                help_text="Option to ping every member of the channel",
                max_length=2,
                verbose_name="channel pings",
            ),
        ),
        migrations.AlterField(
            model_name="tracker",
            name="require_attacker_alliances",
            field=models.ManyToManyField(
                blank=True,
                default=None,
                help_text="only include killmails with attackers from one of these alliances",
                related_name="_tracker_require_attacker_alliances_+",
                to="eveonline.EveAllianceInfo",
            ),
        ),
        migrations.AlterField(
            model_name="tracker",
            name="require_attacker_corporations",
            field=models.ManyToManyField(
                blank=True,
                default=None,
                help_text="only include killmails with attackers from one of these corporations",
                related_name="_tracker_require_attacker_corporations_+",
                to="eveonline.EveCorporationInfo",
            ),
        ),
        migrations.AlterField(
            model_name="tracker",
            name="require_attackers_ship_groups",
            field=models.ManyToManyField(
                blank=True,
                default=None,
                help_text="Only include killmails where at least one attacker is flying one of these ship groups",
                related_name="_tracker_require_attackers_ship_groups_+",
                to="eveuniverse.EveGroup",
            ),
        ),
        migrations.AlterField(
            model_name="tracker",
            name="require_attackers_ship_types",
            field=models.ManyToManyField(
                blank=True,
                default=None,
                help_text="Only include killmails where at least one attacker is flying one of these ship types",
                related_name="_tracker_require_attackers_ship_types_+",
                to="eveuniverse.EveType",
            ),
        ),
        migrations.AlterField(
            model_name="tracker",
            name="require_constellations",
            field=models.ManyToManyField(
                blank=True,
                default=None,
                help_text="Only include killmails that occurred in one of these regions",
                related_name="_tracker_require_constellations_+",
                to="eveuniverse.EveConstellation",
            ),
        ),
        migrations.AlterField(
            model_name="tracker",
            name="require_regions",
            field=models.ManyToManyField(
                blank=True,
                default=None,
                help_text="Only include killmails that occurred in one of these regions",
                related_name="_tracker_require_regions_+",
                to="eveuniverse.EveRegion",
            ),
        ),
        migrations.AlterField(
            model_name="tracker",
            name="require_solar_systems",
            field=models.ManyToManyField(
                blank=True,
                default=None,
                help_text="Only include killmails that occurred in one of these regions",
                related_name="_tracker_require_solar_systems_+",
                to="eveuniverse.EveSolarSystem",
            ),
        ),
        migrations.AlterField(
            model_name="tracker",
            name="require_victim_alliances",
            field=models.ManyToManyField(
                blank=True,
                default=None,
                help_text="only include killmails where the victim belongs to one of these alliances",
                related_name="_tracker_require_victim_alliances_+",
                to="eveonline.EveAllianceInfo",
            ),
        ),
        migrations.AlterField(
            model_name="tracker",
            name="require_victim_corporations",
            field=models.ManyToManyField(
                blank=True,
                default=None,
                help_text="only include killmails where the victim belongs to one of these corporations",
                related_name="_tracker_require_victim_corporations_+",
                to="eveonline.EveCorporationInfo",
            ),
        ),
        migrations.AlterField(
            model_name="tracker",
            name="require_victim_ship_groups",
            field=models.ManyToManyField(
                blank=True,
                default=None,
                help_text="Only include killmails where victim is flying one of these ship groups",
                related_name="_tracker_require_victim_ship_groups_+",
                to="eveuniverse.EveGroup",
            ),
        ),
    ]
