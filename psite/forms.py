from django import forms

from .models import GalleryImage, Email

class GalleryImageForm(forms.ModelForm):
	class Meta:
		model = GalleryImage
		fields = ('picture',)

class EmailForm(forms.ModelForm):
	name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Name'}))
	email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Enter Email'}))
	class Meta:
		model = Email
		fields = ('name', 'email')