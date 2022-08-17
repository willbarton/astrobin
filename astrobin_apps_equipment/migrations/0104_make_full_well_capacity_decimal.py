# Generated by Django 2.2.24 on 2022-08-17 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('astrobin_apps_equipment', '0103_add_mount_control_accessory_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='full_well_capacity',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='sensoreditproposal',
            name='full_well_capacity',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
    ]
