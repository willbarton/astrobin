from datetime import timedelta, datetime

from django.conf import settings
from django.core.cache import cache

from astrobin.enums import SubjectType
from astrobin.fields import COUNTRIES
from astrobin.models import Image
from astrobin.utils import get_client_country_code
from astrobin_apps_images.services import ImageService


def user_language(request):
    d = {
        'user_language': getattr(request, "LANGUAGE_CODE", "en"),
    }
    if request.user.is_authenticated():
        profile = request.user.userprofile
        d['user_language'] = profile.language if profile.language else "en"

    return d


def user_profile(request):
    d = {
        'userprofile': None,
    }

    if request.user.is_authenticated():
        profile = request.user.userprofile
        d['userprofile'] = profile

    return d


def common_variables(request):
    from django_user_agents.utils import get_and_set_user_agent
    from django_bouncy.models import Bounce, Complaint

    get_and_set_user_agent(request)

    hard_bounces = None
    soft_bounces = None
    complained = False

    if request.user.is_authenticated():
        cache_key = 'hard_bounces_%d' % request.user.pk
        hard_bounces = cache.get(cache_key)
        if hard_bounces is None:
            hard_bounces = Bounce.objects.filter(
                hard=True,
                address=request.user.email,
                bounce_type="Permanent")
            cache.set(cache_key, hard_bounces, 3600)

        cache_key = 'soft_bounces_%d' % request.user.pk
        soft_bounces = cache.get(cache_key)
        if soft_bounces is None:
            soft_bounces = Bounce.objects.filter(
                hard=False,
                address=request.user.email,
                bounce_type="Transient",
                created_at__gte=datetime.now() - timedelta(days=7))[:3]
            cache.set(cache_key, soft_bounces, 3600)

        cache_key = 'complained_%d' % request.user.pk
        complained = cache.get(cache_key)
        if complained is None:
            complained = Complaint.objects.filter(address=request.user.email).exists()
            cache.set(cache_key, complained, 3600)

    d = {
        'True': True,
        'False': False,

        'STATIC_URL': settings.STATIC_URL,
        'LANGUAGE_CODE': request.LANGUAGE_CODE if hasattr(request, "LANGUAGE_CODE") else "en",
        'DEBUG_MODE': settings.DEBUG,
        'TESTING': settings.TESTING,
        'REQUEST_COUNTRY': get_client_country_code(request),

        'IMAGES_URL': settings.IMAGES_URL,
        'MEDIA_URL': settings.MEDIA_URL,
        'ADS_ENABLED': settings.ADS_ENABLED,
        'ADMANAGER_PUBLISHER_ID': settings.ADMANAGER_PUBLISHER_ID,
        'NATIVE_RESPONSIVE_WIDE_SLOT': settings.NATIVE_RESPONSIVE_WIDE_SLOT,
        'NATIVE_RESPONSIVE_RECTANGULAR_SLOT': settings.NATIVE_RESPONSIVE_RECTANGULAR_SLOT,
        'NATIVE_RESPONSIVE_RECTANGULAR_SLOT_2': settings.NATIVE_RESPONSIVE_RECTANGULAR_SLOT_2,
        'DONATIONS_ENABLED': settings.DONATIONS_ENABLED,

        'PREMIUM_ENABLED': settings.PREMIUM_ENABLED,

        'PREMIUM_MAX_IMAGES_FREE': settings.PREMIUM_MAX_IMAGES_FREE,
        'PREMIUM_MAX_IMAGES_LITE': settings.PREMIUM_MAX_IMAGES_LITE,

        'PREMIUM_MAX_IMAGES_FREE_2020': settings.PREMIUM_MAX_IMAGES_FREE_2020,
        'PREMIUM_MAX_IMAGES_LITE_2020': settings.PREMIUM_MAX_IMAGES_LITE_2020,
        'PREMIUM_MAX_IMAGES_PREMIUM_2020': settings.PREMIUM_MAX_IMAGES_PREMIUM_2020,

        'PREMIUM_MAX_IMAGE_SIZE_FREE_2020': settings.PREMIUM_MAX_IMAGE_SIZE_FREE_2020,
        'PREMIUM_MAX_IMAGE_SIZE_LITE_2020': settings.PREMIUM_MAX_IMAGE_SIZE_LITE_2020,
        'PREMIUM_MAX_IMAGE_SIZE_PREMIUM_2020': settings.PREMIUM_MAX_IMAGE_SIZE_PREMIUM_2020,

        'PREMIUM_MAX_REVISIONS_FREE_2020': settings.PREMIUM_MAX_REVISIONS_FREE_2020,
        'PREMIUM_MAX_REVISIONS_LITE_2020': settings.PREMIUM_MAX_REVISIONS_LITE_2020,
        'PREMIUM_MAX_REVISIONS_PREMIUM_2020': settings.PREMIUM_MAX_REVISIONS_PREMIUM_2020,

        'PREMIUM_PRICE_FREE_2020': settings.PREMIUM_PRICE_FREE_2020,
        'PREMIUM_PRICE_LITE_2020': settings.PREMIUM_PRICE_LITE_2020,
        'PREMIUM_PRICE_PREMIUM_2020': settings.PREMIUM_PRICE_PREMIUM_2020,
        'PREMIUM_PRICE_ULTIMATE_2020': settings.PREMIUM_PRICE_ULTIMATE_2020,

        'PAYPAL_TEST': settings.PAYPAL_TEST,
        'IOTD_SHOW_CHOOSING_JUDGE': settings.IOTD_SHOW_CHOOSING_JUDGE,
        'ENABLE_SOLVING': settings.ENABLE_SOLVING,
        'GOOGLE_ANALYTICS_ID': settings.GOOGLE_ANALYTICS_ID,
        'GOOGLE_ADS_ID': settings.GOOGLE_ADS_ID,
        'READONLY_MODE': settings.READONLY_MODE,
        'HARD_BOUNCES': hard_bounces,
        'SOFT_BOUNCES': soft_bounces,
        'HAS_COMPLAINT': complained,
        'COUNTRIES': COUNTRIES,
        'COOKIELAW_ACCEPTED': request.COOKIES.get('cookielaw_accepted', False),
        'AUTOMATIC_RECOVERY_CONFIRMATION_BEGINS': Image.all_objects.filter(
            user=request.user,
            corrupted=True,
            recovered__isnull=False).order_by('recovered').first().recovered + timedelta(days=14) \
            if request.user.is_authenticated() and \
               Image.all_objects.filter(
                   user=request.user,
                   corrupted=True,
                   recovered__isnull=False).exists() \
            else None,

        'enums': {
            'SubjectType': SubjectType,
        },
    }

    if request.user.is_authenticated() and request.user.userprofile.is_image_moderator():
        d['images_pending_moderation_no'] = ImageService().get_images_pending_moderation().count()

    return d
