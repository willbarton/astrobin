# Generated by Django 2.2.24 on 2024-07-02 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('astrobin_apps_equipment', '0162_equipmentitemmarketplacelistinglineitemimage_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipmentitemmarketplacelisting',
            name='listing_type',
            field=models.CharField(choices=[('WANTED', 'Wanted'), ('FOR_SALE', 'For sale')], default='FOR_SALE', max_length=8),
        ),
    ]
