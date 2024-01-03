from django import forms

from .models import User


class UserForm(forms.ModelForm):
	class Meta:
		model=User
		fields=['username', 'email', 'password', 'phone', 'photo']

	def save(self, commit=True):
		odom=super().save(commit)
		odom.set_password(self.cleaned_data['password'])
		odom.save()
		return odom


class SigninForm(forms.Form):
	username=forms.CharField(max_length=18)
	password=forms.CharField(max_length=18)