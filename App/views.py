from .models import UserProfile
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import UserForm, UpdateUser, UpdateProfile
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
# Create your views here.


def Home(request):
    if request.user.is_authenticated:
        user = request.user
        user, created = UserProfile.objects.get_or_create(user=user)

    u_profile = UserProfile.objects.all()
    return render(request, 'main/Home.html', context={'profile': u_profile})


def SignUp_function(request):
    if request.method == 'POST':
        forms = UserForm(request.POST)
        if forms.is_valid():
            user = forms.save()
            login(request, user)
            messages.success(request, 'Good Job :)')
            return redirect('App:Home')
        messages.error(request, 'Something went to wrong :( ')
    forms = UserForm()
    return render(request, 'register/signup.html', context={'forms': forms})


def Login_function(request):
    if request.method == 'POST':
        forms = AuthenticationForm(request, data=request.POST)
        if forms.is_valid():
            username = forms.cleaned_data.get('username')
            password = forms.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Good Job :) {user.username}')
                return redirect('App:Home')
            else:
                messages.error(request, 'Error :( ')
        else:
            messages.error(request, 'Error :( ')
    forms = AuthenticationForm
    return render(request, 'register/login.html', context={'login_form': forms})


def LogOut_function(request):
    logout(request)
    messages.info(request, 'Good Bie')
    return redirect('App:Home')


@login_required
def Update_function(request):
    if request.method == 'POST':
        u_user = UpdateUser(request.POST, instance=request.user)
        u_profile = UpdateProfile(
            request.POST, request.FILES, instance=request.user.userprofile)
        if u_user.is_valid() and u_profile.is_valid():
            u_user.save()
            u_profile.save()
            print('com')
            messages.success(request, 'Updated USER')
            return redirect('App:Home')
    else:
        print('error')
        u_user = UpdateUser(instance=request.user)
        u_profile = UpdateProfile(instance=request.user.userprofile)

    context = {
        'u_user': u_user,
        'u_profile': u_profile,
    }
    return render(request, 'register/settings.html', context)
