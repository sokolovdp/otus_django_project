from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from main_app.forms import UserForm, UserProfileInfoForm
from .logger import django_logger

django_logger.info('----START----')


def index(request):
    context = {'active': "home"}
    return render(request, 'index.html', context=context)


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('ACCOUNT IS NOT ACTIVE!')
        else:
            django_logger.info(f'invalid login: "{username}" password: "{password}"')
            return HttpResponse('INVALID USERNAME OR PASSWORD!')
    else:
        context = {'active': "login"}
        return render(request, 'login.html', context=context)


def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)  # hash password
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user  # One to One relation

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        registered = True if request.user.username else False
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    context = {
        'active': 'register',
        'user_form': user_form,
        'profile_form': profile_form,
        'registered': registered
    }
    return render(request, 'registration.html', context=context)
