from datetime import datetime

from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

# from rest_framework.authentication import SessionAuthentication
# from rest_framework.permissions import IsAuthenticated


from otus_django_project import settings

from main_app.models import UserProfileInfo
from main_app.serializers import UserProfileInfoSerializer


class VersionView(APIView):

    def get(self, request):
        result = settings.APPLICATION_VERSION
        uptime = datetime.now() - result['started']
        result['uptime_seconds'] = uptime.seconds
        settings.django_logger.info(f'Version API test: {result}')
        return Response(result)


class UserProfileView(ListAPIView):
    # authentication_classes = (SessionAuthentication,)
    # permission_classes = (IsAuthenticated,)

    queryset = UserProfileInfo.objects
    serializer_class = UserProfileInfoSerializer

