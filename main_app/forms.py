from django import forms
from django.contrib.auth.models import User

from main_app.models import UserProfileInfo, ItemModel


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')


class ItemInfoForm(forms.ModelForm):
    class Meta:
        model = ItemModel
        fields = '__all__'
