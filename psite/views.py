from django.shortcuts import render

from .forms import EmailForm
from .models import GalleryImage, Track


def home_page(request):
	if request.method == 'POST':
		form = EmailForm(request.POST)
		if form.is_valid():
			form.save()
			form = EmailForm()
	else:
		form = EmailForm()

	context = {'form': form}
	return render(request, 'home.html', context)

def gallery(request):
	images = GalleryImage.objects.all()
	context = {'images': images}
	return render(request, 'gallery.html', context)

def tracks(request):
	tracks = Track.objects.all().order_by('-date_added')
	context = {'tracks': tracks}
	return render(request, 'music.html', context)