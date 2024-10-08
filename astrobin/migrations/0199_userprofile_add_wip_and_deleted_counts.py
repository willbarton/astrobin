# Generated by Django 2.2.24 on 2024-02-22 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('astrobin', '0198_userprofile_image_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='deleted_image_count',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='wip_image_count',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
    ]
