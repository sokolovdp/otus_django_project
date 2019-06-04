from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from otus_django_project import settings
from datetime import datetime


class Version(APIView):
    # authentication_classes = (SessionAuthentication,)
    # permission_classes = (IsAuthenticated,)

    def get(self, request):
        # user = request.user.username
        result = settings.APPLICATION_VERSION
        uptime = datetime.now() - result['started']
        result['uptime_seconds'] = uptime.seconds
        settings.django_logger.info(f'Version API test: {result}')
        return Response(result)
