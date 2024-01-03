from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate

from .models import User
from .forms import UserForm, SigninForm


def home(request):
	odomlar=User.objects.all()
	return render(request, 'home.html', {'odomlar':odomlar})


def Signup(request):
	forma=UserForm()
	if request.method=='POST':
		forma=UserForm(data=request.POST, files=request.FILES)
		if forma.is_valid():
			forma.save()
			return redirect('home')
		return render(request, 'signup.html', {'forma':forma})
	return render(request, 'signup.html', {'forma':forma})


def Signin(request):
	Login=SigninForm()
	if request.method=='POST':
		Login=SigninForm(data=request.POST)
		if Login.is_valid():
			odomism=request.POST.get('username')
			parol=request.POST.get('password')
			odom=authenticate(username=odomism, password=parol)
			if odom is not None:
				login(request, odom)
				return redirect('home')
		return render(request, 'signin.html', {'Login':Login})
	return render(request, 'signin.html', {'Login':Login})


def Logout(request):
	logout(request)
	return redirect('home')


def Profile(request, id):
	user=User.objects.get(id=id)
	profile=UserForm(instance=request.user)
	return render(request, 'profile.html', {'user':user})
