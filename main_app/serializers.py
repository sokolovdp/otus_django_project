from rest_framework import serializers

from main_app.models import UserProfileInfo, ItemModel


class UserProfileInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfileInfo
        fields = '__all__'


class ItemModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = ItemModel
        fields = '__all__'
