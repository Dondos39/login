from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


from myapp.models import *
from . import forms
from myapp.forms import UserForm, UserInfoForm

def index(request):
    user_list = User.objects.order_by('username')
    user_dict = {'User_records': user_list}
    return render(request, 'myapp/homepage.html', context=user_dict)

def user_login(request):
    form = UserForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponseRedirect("Account not active.")
        else:
            print(f"Username: {username} Password: {password}")
            return HttpResponseRedirect("Invalid credentials.")

    return render(request, 'myapp/login_page.html', {})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        user_info_form = UserInfoForm(data=request.POST)

        if user_form.is_valid() and user_info_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            user_info = user_info_form.save(commit=False)
            user_info.user = user

            if 'prof_pic' in request.FILES:
                user_info.prof_pic = request.FILES['prof_pic']

            user_info.save()
            registered = True
        else:
            print(user_form.errors, user_info_form.errors)
    else:
        user_form = UserForm()
        user_info_form = UserInfoForm()

    return render(request, 'myapp/registration.html', {'user_form': user_form,
                                                       'user_info_form': user_info_form,
                                                       'registered': registered})
