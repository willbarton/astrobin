from datetime import timedelta

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from astrobin.models import Image
from astrobin_apps_images.services import ImageService
from astrobin_apps_iotd.models import Iotd, IotdSubmission, IotdVote
from astrobin_apps_iotd.services import IotdService
from common.services import DateTimeService


@receiver(post_save, sender=Iotd)
def iotd_post_save(sender, instance: Iotd, created: bool, **kwargs):
    if created:
        Image.objects.filter(pk=instance.image.pk).update(updated=DateTimeService.now())
        ImageService(instance.image).clear_badges_cache()


@receiver(post_save, sender=IotdVote)
def iotd_vote_post_save(sender, instance: IotdVote, created: bool, **kwargs):
    if created:
        check_activity_level_and_update_reminders_count(sender, instance)
        check_and_send_notification_for_enough_votes(instance.image)


@receiver(post_save, sender=IotdSubmission)
def iotd_submission_post_save(sender, instance: IotdSubmission, created: bool, **kwargs):
    if created:
        check_activity_level_and_update_reminders_count(sender, instance)
        check_and_send_notification_for_enough_submissions(instance.image)


def check_and_send_notification_for_enough_submissions(image: Image):
    min_promotions = getattr(settings, 'IOTD_SUBMISSION_MIN_PROMOTIONS', 3)
    if image.iotdsubmission_set.count() == min_promotions:
        IotdService.notify_about_reaching_enough_iotd_submissions(image)


def check_and_send_notification_for_enough_votes(image: Image):
    min_promotions = getattr(settings, 'IOTD_REVIEW_MIN_PROMOTIONS', 3)
    if image.iotdvote_set.count() == min_promotions:
        IotdService.notify_about_reaching_enough_iotd_votes(image)


def check_activity_level_and_update_reminders_count(sender, instance):
    min_promotions_per_period = getattr(settings, 'IOTD_MIN_PROMOTIONS_PER_PERIOD', '7/7')
    min_promotions = int(min_promotions_per_period.split('/')[0])
    days = int(min_promotions_per_period.split('/')[1])
    property_name = 'reviewer' if hasattr(instance, 'reviewer') else 'submitter'

    promotions = sender.objects.filter(
        **{
            property_name: getattr(instance, property_name),
            'date__gte': DateTimeService.now() - timedelta(days=days)
        }
    ).count()

    if promotions >= min_promotions:
        # Reset the counter as this user has been sufficiently active.
        getattr(instance, property_name).userprofile.insufficiently_active_iotd_staff_member_reminders_sent = 0
        getattr(instance, property_name).userprofile.save(keep_deleted=True)
