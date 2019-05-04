from rest_framework.views import APIView
from rest_framework.response import Response

from main_app.logger import django_logger


class Test(APIView):
    permission_classes = []
    authentication_classes = []

    def get(self, request):
        django_logger.info('Test API')
        return Response({"test": 12345})
