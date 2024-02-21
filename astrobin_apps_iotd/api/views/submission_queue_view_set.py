# -*- coding: utf-8 -*-


from djangorestframework_camel_case.render import CamelCaseJSONRenderer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import BrowsableAPIRenderer

from astrobin_apps_iotd.api.queue_pagination import QueuePagination
from astrobin_apps_iotd.api.serializers.submission_queue_serializer import SubmissionQueueSerializer
from astrobin_apps_iotd.services import IotdService
from common.constants import GroupName
from common.permissions import ReadOnly, is_group_member


class SubmissionQueueViewSet(viewsets.ModelViewSet):
    serializer_class = SubmissionQueueSerializer
    renderer_classes = [BrowsableAPIRenderer, CamelCaseJSONRenderer]
    pagination_class = QueuePagination
    permission_classes = [IsAuthenticated, ReadOnly, is_group_member(GroupName.IOTD_SUBMITTERS)]
    http_method_names = ['get', 'head']

    def get_queryset(self):
        return IotdService().get_submission_queue(
            self.request.user,
            self.request.GET.get('sort', None),
        )
