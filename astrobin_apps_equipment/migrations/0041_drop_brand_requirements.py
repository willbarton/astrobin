# Generated by Django 2.2.24 on 2021-11-25 13:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('astrobin_apps_equipment', '0040_add_field_group_to_equipment_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessory',
            name='brand',
            field=models.ForeignKey(
                null=True, blank=True, on_delete=django.db.models.deletion.PROTECT,
                related_name='astrobin_apps_equipment_brand_accessorys', to='astrobin_apps_equipment.EquipmentBrand'
            ),
        ),
        migrations.AlterField(
            model_name='accessoryeditproposal',
            name='brand',
            field=models.ForeignKey(
                null=True, blank=True, on_delete=django.db.models.deletion.PROTECT,
                related_name='astrobin_apps_equipment_brand_accessoryeditproposals',
                to='astrobin_apps_equipment.EquipmentBrand'
            ),
        ),
        migrations.AlterField(
            model_name='camera',
            name='brand',
            field=models.ForeignKey(
                null=True, blank=True, on_delete=django.db.models.deletion.PROTECT,
                related_name='astrobin_apps_equipment_brand_cameras', to='astrobin_apps_equipment.EquipmentBrand'
            ),
        ),
        migrations.AlterField(
            model_name='cameraeditproposal',
            name='brand',
            field=models.ForeignKey(
                null=True, blank=True, on_delete=django.db.models.deletion.PROTECT,
                related_name='astrobin_apps_equipment_brand_cameraeditproposals',
                to='astrobin_apps_equipment.EquipmentBrand'
            ),
        ),
        migrations.AlterField(
            model_name='filter',
            name='brand',
            field=models.ForeignKey(
                null=True, blank=True, on_delete=django.db.models.deletion.PROTECT,
                related_name='astrobin_apps_equipment_brand_filters', to='astrobin_apps_equipment.EquipmentBrand'
            ),
        ),
        migrations.AlterField(
            model_name='filtereditproposal',
            name='brand',
            field=models.ForeignKey(
                null=True, blank=True, on_delete=django.db.models.deletion.PROTECT,
                related_name='astrobin_apps_equipment_brand_filtereditproposals',
                to='astrobin_apps_equipment.EquipmentBrand'
            ),
        ),
        migrations.AlterField(
            model_name='mount',
            name='brand',
            field=models.ForeignKey(
                null=True, blank=True, on_delete=django.db.models.deletion.PROTECT,
                related_name='astrobin_apps_equipment_brand_mounts', to='astrobin_apps_equipment.EquipmentBrand'
            ),
        ),
        migrations.AlterField(
            model_name='mounteditproposal',
            name='brand',
            field=models.ForeignKey(
                null=True, blank=True, on_delete=django.db.models.deletion.PROTECT,
                related_name='astrobin_apps_equipment_brand_mounteditproposals',
                to='astrobin_apps_equipment.EquipmentBrand'
            ),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='brand',
            field=models.ForeignKey(
                null=True, blank=True, on_delete=django.db.models.deletion.PROTECT,
                related_name='astrobin_apps_equipment_brand_sensors', to='astrobin_apps_equipment.EquipmentBrand'
            ),
        ),
        migrations.AlterField(
            model_name='sensoreditproposal',
            name='brand',
            field=models.ForeignKey(
                null=True, blank=True, on_delete=django.db.models.deletion.PROTECT,
                related_name='astrobin_apps_equipment_brand_sensoreditproposals',
                to='astrobin_apps_equipment.EquipmentBrand'
            ),
        ),
        migrations.AlterField(
            model_name='software',
            name='brand',
            field=models.ForeignKey(
                null=True, blank=True, on_delete=django.db.models.deletion.PROTECT,
                related_name='astrobin_apps_equipment_brand_softwares', to='astrobin_apps_equipment.EquipmentBrand'
            ),
        ),
        migrations.AlterField(
            model_name='softwareeditproposal',
            name='brand',
            field=models.ForeignKey(
                null=True, blank=True, on_delete=django.db.models.deletion.PROTECT,
                related_name='astrobin_apps_equipment_brand_softwareeditproposals',
                to='astrobin_apps_equipment.EquipmentBrand'
            ),
        ),
        migrations.AlterField(
            model_name='telescope',
            name='brand',
            field=models.ForeignKey(
                null=True, blank=True, on_delete=django.db.models.deletion.PROTECT,
                related_name='astrobin_apps_equipment_brand_telescopes', to='astrobin_apps_equipment.EquipmentBrand'
            ),
        ),
        migrations.AlterField(
            model_name='telescopeeditproposal',
            name='brand',
            field=models.ForeignKey(
                null=True, blank=True, on_delete=django.db.models.deletion.PROTECT,
                related_name='astrobin_apps_equipment_brand_telescopeeditproposals',
                to='astrobin_apps_equipment.EquipmentBrand'
            ),
        ),
    ]
