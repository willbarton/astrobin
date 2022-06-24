# Generated by Django 2.2.24 on 2022-06-24 19:20

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('astrobin_apps_equipment', '0080_fix_unique_constraint_of_filter_migration_record'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='deepskyacquisitionmigrationrecord',
            unique_together={('deep_sky_acquisition', 'from_gear', 'deleted')},
        ),
    ]
