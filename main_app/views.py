from django.shortcuts import render
from main_app.forms import UserForm, UserProfileInfoForm

from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def index(request):
    context = {}
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
            print("!!! invalid login -> " + username + " : " + password)
            return HttpResponse('INVALID USERNAME OR PASSWORD!')
    else:
        return render(request, 'login.html', {})


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
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    context = {'user_form': user_form,
               'profile_form': profile_form,
               'registered': registered}
    return render(request, 'registration.html', context=context)
