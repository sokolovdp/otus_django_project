from rest_framework import serializers

from main_app.models import UserProfileInfo


class UserProfileInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfileInfo
        fields = '__all__'
