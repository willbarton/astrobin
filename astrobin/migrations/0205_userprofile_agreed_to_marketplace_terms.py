# Generated by Django 2.2.24 on 2024-06-30 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('astrobin', '0204_add_starfront_observatories_to_remote_sources'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='agreed_to_marketplace_terms',
            field=models.DateTimeField(blank=True, editable=False, null=True),
        ),
    ]
