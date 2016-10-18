from django import forms

from .models import GalleryImage, Register

class GalleryImageForm(forms.ModelForm):
	class Meta:
		model = GalleryImage
		fields = ('picture',)

class RegisterForm(forms.ModelForm):
	name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Name'}))
	email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Enter Email'}))
	class Meta:
		model = Register
		fields = ('name', 'email')