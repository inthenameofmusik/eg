from django.shortcuts import render

import subprocess

from .forms import RegisterForm
from .models import GalleryImage, Track, EditableText


def home_page(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			form = RegisterForm()
	else:
		form = RegisterForm()

	latest_track = Track.objects.first()

	news = EditableText.objects.get(section__iexact='News')
	bio = EditableText.objects.get(section__iexact='Bio')

	context = {'form': form, 'latest_track': latest_track, 'news': news, 'bio': bio}
	return render(request, 'home.html', context)

def gallery(request):
	images = GalleryImage.objects.all()
	context = {'images': images}
	email = 'echo "%s" | mail -s "This is the subject line" pomuzaxix@hostcalls.com' % ('living life oh yes', )
	subprocess.call(email, shell=True)
	return render(request, 'gallery.html', context)

def tracks(request):
	tracks = Track.objects.all().order_by('-date_added')
	context = {'tracks': tracks}
	return render(request, 'music.html', context)