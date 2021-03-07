from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from . import forms, models
from .forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}! You are logged in.')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    """Display User Profile"""
    profile = request.user.profile
    return render(request, 'users/profile.html', {
        'profile': profile
    })


@login_required
def edit_profile(request):
    user = request.user
    profile = get_object_or_404(models.Profile, user=user)
    form = forms.ProfileForm(instance=profile)

    if request.method == 'POST':
        form = forms.ProfileForm(instance=profile, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()

            messages.success(request, "Updated the Profile Successfully!")
            return HttpResponseRedirect(reverse('users:profile'))

    return render(request, 'users/editprofile.html', {
        'form': form
    })
