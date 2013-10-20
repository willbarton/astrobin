# Python
import simplejson

# Django
from django.contrib.contenttypes.models import ContentType
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import base

# restframework
from rest_framework import generics
from rest_framework import permissions

# This app
from astrobin_apps_platesolving.models import Solution
from astrobin_apps_platesolving.serializers import SolutionSerializer
from astrobin_apps_platesolving.solver import Solver


class SolveView(base.View):
    def post(self, request, *args, **kwargs):
        object_id = kwargs.pop('object_id')
        content_type_id = kwargs.pop('content_type_id')

        content_type = ContentType.objects.get_for_id(content_type_id)
        target = get_object_or_404(content_type.model_class(), pk = object_id)
        solution, created = Solution.objects.get_or_create(object_id = object_id, content_type = content_type)

        if solution.submission_id is None:
            solver = Solver()
            thumb = target.thumbnail_raw('regular')
            submission = solver.solve(thumb.file)
            solution.status = Solver.PENDING
            solution.submission_id = submission
            solution.save()

        context = {
            'solution': solution.id,
            'submission': solution.submission_id,
        }
        return HttpResponse(simplejson.dumps(context), mimetype='application/json')


class SolutionUpdateView(base.View):
    def post(self, request, *args, **kwargs):
        solution = get_object_or_404(Solution, pk = kwargs.pop('pk'))
        solver = Solver()
        status = solver.status(solution.submission_id)

        if status == Solver.MISSING:
            solution.status = status
            solution.save()

        context = {'status': status}
        return HttpResponse(simplejson.dumps(context), mimetype='application/json')


class SolutionFinalizeView(base.View):
    def post(self, request, *args, **kwargs):
        solution = get_object_or_404(Solution, pk = kwargs.pop('pk'))
        solver = Solver()
        solution.status = solver.status(solution.submission_id)

        if solution.status == Solver.SUCCESS:
            import urllib2
            from django.core.files import File
            from django.core.files.temp import NamedTemporaryFile

            info = solver.info(solution.submission_id)

            solution.objects_in_field = ', '.join(info['objects_in_field'])

            solution.ra          = "%.3f" % info['calibration']['ra']
            solution.dec         = "%.3f" % info['calibration']['dec']
            solution.pixscale    = "%.3f" % info['calibration']['pixscale']
            solution.orientation = "%.3f" % info['calibration']['orientation']
            solution.radius      = "%.3f" % info['calibration']['radius']

            url = solver.annotated_image_url(solution.submission_id)
            img = NamedTemporaryFile(delete=True)
            img.write(urllib2.urlopen(url).read())
            img.flush()
            img.seek(0)
            f = File(img)

            target = solution.content_type.get_object_for_this_type(pk = solution.object_id)
            solution.image_file.save(target.image_file.name, f)

        solution.save()

        context = {'status': solution.status}
        return HttpResponse(simplejson.dumps(context), mimetype='application/json')


###############################################################################
# API                                                                         #
###############################################################################


class SolutionList(generics.ListCreateAPIView):
    model = Solution
    queryset = Solution.objects.order_by('pk')
    serializer_class = SolutionSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class SolutionDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Solution
    serializer_class = SolutionSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

