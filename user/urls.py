from django.contrib import admin
from django.urls import path

from .views import home, Signup, Signin, Logout, Profile


urlpatterns=[
	
	path('sign-up/', Signup, name='signup'),
	path('sign-in/', Signin, name='signin'),
	path('log-out/', Logout, name='Logout'),
	path('profile/<int:id>', Profile, name='profile'),

]