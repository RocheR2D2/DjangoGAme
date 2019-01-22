from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib import messages 
from .forms import SignUpForm, EditUserForm
from authenticate.models import UserProfile
from authenticate.forms import UserProfileForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def index(request):

    my_dict = {'insert_me' : "Im coming form first app/index.html!"}
    return render(request, 'index.html', context=my_dict)

def login_user(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, ('You have already been logged in'))
			return redirect('index')
		else:
			messages.success(request, ('Error, please try again'))
			return redirect('login')
	else:
		return render(request, 'registration/login.html', {})


def logout_user(request):
	logout(request)
	messages.success(request, ('You have been logged out'))
	return redirect('index')

def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request,user)
			messages.success(request, ('You Have Registered... This is your first deck'))
			return redirect('first_deck')
	else:
		form = SignUpForm()
	
	context = {'form': form}
	return render(request, 'registration/register.html', context)

@login_required
def edit_user(request):

	if request.method == 'POST':
		form = EditUserForm(request.POST, instance=request.user)
		profile_form = UserProfileForm(request.POST, instance=request.user.userprofile)

		if form.is_valid() and profile_form.is_valid():
			user = form.save()
			user.save()
			profile = profile_form.save(commit=False)
			profile.user = user
			if 'profile' in request.FILES:
				profile.profile = request.FILES['profile']

			profile.save()
			messages.success(request, ('You Have Edited Your Profile'))
			return redirect('index')
	else:
		form = EditUserForm(instance=request.user)
		profile_form = UserProfileForm(instance=request.user.userprofile)

	
	context = {'form': form, 'profile_form': profile_form}
	return render(request, 'registration/edituser.html', context)


def change_password(request):

	if request.method == 'POST':
		form = PasswordChangeForm(data=request.POST, user=request.user)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			messages.success(request, ('You have reset your password...'))
			return redirect('index')
	else:
		form = PasswordChangeForm(user=request.user)
	
	context = {'form': form}
	return render(request, 'registration/change_password.html', context)


def custom_user(request):
	profiles = UserProfile.objects.all

	return render(request, 'customuser.html', {'profiles': profiles})

@login_required
def user_profile(request, username):

	viewuser = User.objects.get(username=username)

	return render(request, 'registration/user_profile.html', {'viewuser': viewuser})

