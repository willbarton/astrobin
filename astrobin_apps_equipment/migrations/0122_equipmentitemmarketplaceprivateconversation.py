# Generated by Django 2.2.24 on 2023-12-12 18:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('astrobin_apps_equipment', '0121_equipmentitemmarketplaceoffer'),
    ]

    operations = [
        migrations.CreateModel(
            name='EquipmentItemMarketplacePrivateConversation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('listing', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='private_conversations', to='astrobin_apps_equipment.EquipmentItemMarketplaceListing')),
                ('user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='equipment_item_marketplace_listings_private_conversations', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
