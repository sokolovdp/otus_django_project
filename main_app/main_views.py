from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from main_app.forms import UserForm, UserProfileInfoForm
from main_app.models import ItemModel
from otus_django_project.settings import django_logger

django_logger.info('----START----')


def index_view(request):
    context = {'active': "home"}
    return render(request, 'index.html', context=context)


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def user_login(request):
    errors_string = None
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                errors_string = 'ACCOUNT IS NOT ACTIVE!'
        else:
            django_logger.info(f'invalid login: "{username}" password: "{password}"')
            errors_string = 'INVALID USERNAME OR PASSWORD!'

    context = {'active': "login", 'errors': errors_string}
    return render(request, 'login.html', context=context)


def register(request):
    registered = False
    errors_string = None

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
            all_errors = []
            for err_list in user_form.errors.values():
                all_errors.append(' '.join(err_list))
            for err_list in profile_form.errors.values():
                all_errors += ' '.join(err_list)
            errors_string = ' '.join(all_errors)
    else:
        registered = True if request.user.username else False
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    context = {
        'active': 'register',
        'errors': errors_string,
        'user_form': user_form,
        'profile_form': profile_form,
        'registered': registered
    }
    return render(request, 'registration.html', context=context)


@login_required
def items_list(request):
    context = {
        'items': list(ItemModel.objects.all())
    }
    return render(request, 'items_list.html', context=context)


@login_required
def item_view(request, pk):
    context = {
        'item': ItemModel.objects.get(pk=pk)
    }
    return render(request, 'item_detail.html', context=context)
