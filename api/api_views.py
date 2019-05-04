from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from main_app.logger import django_logger


class Test(APIView):
    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = request.user.username
        django_logger.info(f'Test API user: {user}')
        return Response({"test user": user})
