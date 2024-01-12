# Generated by Django 2.2.24 on 2024-01-12 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('astrobin', '0188_image_disqualified_from_iotd_tp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='remote_source',
            field=models.CharField(blank=True, choices=[(None, '---------'), ('OWN', 'Non-commercial independent facility'), (None, '---------'), ('ALNI', 'Alnitak Remote Observatories'), ('AC', 'AstroCamp'), ('AHK', 'Astro Hostel Krasnodar'), ('ACRES', 'Astronomy Acres'), ('AOWA', 'Astro Observatories Western Australia'), ('ATLA', 'Atlaskies Observatory'), ('CS', 'ChileScope'), ('DMA', 'Dark Matters Astrophotography'), ('DSNM', 'Dark Sky New Mexico'), ('DSP', 'Dark Sky Portal'), ('DSV', 'Deepsky Villa'), ('DSC', 'DeepSkyChile'), ('DSPR', 'Deep Space Products Remote'), ('DSW', 'DeepSkyWest'), ('eEyE', 'e-EyE Extremadura'), ('EITS', 'Eye In The Sky'), ('GFA', 'Goldfield Astronomical Observatory'), ('GMO', 'Grand Mesa Observatory'), ('HAKOS', 'Hakos Astro Farm'), ('HMO', "Heaven's Mirror Observatory"), ('IC', 'IC Astronomy Observatories'), ('ITU', 'Image The Universe'), ('INS', 'Insight Observatory'), ('ITELESCO', 'iTelescope'), ('LGO', 'Lijiang Gemini Observatory'), ('MARIO', 'Marathon Remote Imaging Observatory (MaRIO)'), ('NMS', 'New Mexico Skies'), ('OES', 'Observatorio El Sauce'), ('PSA', 'PixelSkies'), ('REM', 'RemoteSkies.net'), ('REMSG', 'Remote Skygems'), ('RLD', 'Riverland Dingo Observatory'), ('ROBO', 'RoboScopes'), ('SS', 'Sahara Sky'), ('SPVO', 'San Pedro Valley Observatory'), ('SRO', 'Sierra Remote Observatories'), ('SRO2', 'Sky Ranch Observatory'), ('SPOO', 'SkyPi Remote Observatory'), ('SLO', 'Slooh'), ('SPI', 'Spica'), ('SSLLC', 'Stellar Skies LLC'), ('SKIESAWAY', 'SkiesAway Remote Observatories'), ('TAIYUGE', 'TaiYuge Observatory'), ('TELI', 'Telescope Live'), ('TREV', 'Trevinca Skies'), ('UDRO', 'Utah Desert Remote Observatories'), ('WTO', 'West Texas Observatory (WTO)'), ('YINHE', 'YinHe Observatory'), ('YUNLING', 'Yunling Observatory'), ('OTHER', 'None of the above')], help_text='Which remote hosting facility did you use to acquire data for this image?', max_length=10, null=True, verbose_name='Remote data source'),
        ),
    ]
