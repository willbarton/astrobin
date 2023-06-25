# Generated by Django 2.2.24 on 2023-06-25 07:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('astrobin_apps_platesolving', '0023_add_show_hd_and_max_magnitude_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='platesolvingsettings',
            name='downsample_factor',
            field=models.DecimalField(
                blank=True, decimal_places=2,
                help_text='Downsample (bin) your image by this factor before performing source detection. This often helps with saturated images, noisy images, and large images. 2 and 4 are commonly-useful values.',
                max_digits=4, null=True, validators=[django.core.validators.MinValueValidator(1.01),
                                                     django.core.validators.MaxValueValidator(99.99)],
                verbose_name='Downsample factor'
            ),
        ),
        migrations.AddField(
            model_name='platesolvingsettings',
            name='use_sextractor',
            field=models.BooleanField(
                default=False,
                help_text="Use the SourceExtractor program to detect stars, not Nova's built-in program.",
                verbose_name='Use SExtractor'
            ),
        ),
    ]
