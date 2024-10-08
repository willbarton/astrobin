# -*- coding: utf-8 -*-

import logging
from datetime import datetime, timedelta

from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.http import HttpResponseForbidden
from django.utils.translation import ugettext_lazy as _
from djangorestframework_camel_case.render import CamelCaseJSONRenderer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import BrowsableAPIRenderer
from rest_framework.response import Response

from astrobin_apps_iotd.api.serializers.vote_serializer import VoteSerializer
from astrobin_apps_iotd.models import IotdReviewerSeenImage, IotdVote
from common.constants import GroupName
from common.permissions import is_group_member


log = logging.getLogger(__name__)


class VoteViewSet(viewsets.ModelViewSet):
    serializer_class = VoteSerializer
    renderer_classes = [BrowsableAPIRenderer, CamelCaseJSONRenderer]
    pagination_class = None
    permission_classes = [IsAuthenticated, is_group_member(GroupName.IOTD_REVIEWERS)]
    model = IotdVote

    def get_queryset(self):
        return self.model.objects.filter(
            reviewer=self.request.user,
            date__contains=datetime.now().date())

    def create(self, request, *args, **kwargs):
        try:
            result = super(viewsets.ModelViewSet, self).create(request, *args, **kwargs)
            try:
                IotdReviewerSeenImage.objects.get_or_create(
                    submitter=request.user,
                    image=result.data.get("image"),
                )
            except:
                log.error(f"Error creating IotdReviewerSeenImage when creating IotdVote for user {request.user}")
            return result
        except ValidationError as e:
            log.error(f"ValidationError with user {request.user} creating IotdVote: " + str(e))
            return HttpResponseForbidden(e.messages)
        except IntegrityError:
            return Response(status=204)

    def destroy(self, request, *args, **kwargs):
        vote = self.get_object()  # type: IotdVote
        deadline = datetime.now() - timedelta(days=settings.IOTD_REVIEW_WINDOW_DAYS)

        if vote.reviewer != request.user:
            return HttpResponseForbidden(["You cannot delete another user's vote."])

        if vote.date < deadline or vote.image.submitted_for_iotd_tp_consideration < deadline:
            return HttpResponseForbidden([_("Sorry, it's now too late to retract this vote.")])

        return super(viewsets.ModelViewSet, self).destroy(request, *args, **kwargs)
