from django import forms

from .models import GalleryImage, Register, Message

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

class MessageForm(forms.ModelForm):
	mfrom = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Enter your email', 'class': 'mform mfrom'}))
	msubject = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter a subject', 'class': 'mform msubject'}))
	mcontent = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter your message', 'class': 'mform mcontent'}))
	class Meta:
		model = Message
		fields = ('mfrom', 'msubject', 'mcontent')