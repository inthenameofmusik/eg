from django.shortcuts import render
from django.core.mail import send_mail

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
	send_mail(
		'Subject doe',
		'yep doe',
		'root@eg-nyc2',
		['pomuzaxix@hostcalls.com'],
		fail_silently=False,
	)
	return render(request, 'gallery.html', context)

def tracks(request):
	tracks = Track.objects.all().order_by('-date_added')
	context = {'tracks': tracks}
	return render(request, 'music.html', context)