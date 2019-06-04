from datetime import datetime

from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework import status

# from rest_framework.authentication import SessionAuthentication
# from rest_framework.permissions import IsAuthenticated


from otus_django_project import settings

from main_app.models import UserProfileInfo, ItemModel
from main_app.serializers import UserProfileInfoSerializer, ItemModelSerializer


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


class ItemViewSet(ViewSet):
    # authentication_classes = (SessionAuthentication,)
    # permission_classes = (IsAuthenticated,)

    queryset = ItemModel.objects
    serializer_class = ItemModelSerializer

    def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        item = self.queryset.filter(id=pk).first()
        return Response(self.serializer_class(item).data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_item = serializer.create(validated_data=serializer.validated_data)
        return Response(self.serializer_class(new_item).data)

    def update(self, request, pk=None):
        item = self.queryset.filter(pk=pk).first()
        if item:
            serializer = self.serializer_class(item, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        item = self.queryset.filter(pk=pk).first()
        if item:
            item.delete()
            return Response(self.serializer_class(item).data)
        else:
            return Response({}, status=status.HTTP_404_NOT_FOUND)


