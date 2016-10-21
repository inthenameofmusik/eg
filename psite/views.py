from django.shortcuts import render, redirect


from .forms import RegisterForm, MessageForm
from .models import GalleryImage, Track, EditableText


def send_message(request):
	if request.method == 'POST':
		form = MessageForm(request.POST)
		if form.is_valid():
			form.save()
	return redirect('homepage')


def home_page(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			form = RegisterForm()
	else:
		form = RegisterForm()

	latest_track = Track.objects.all().order_by('-date_added').first()

	mform = MessageForm()

	news = EditableText.objects.get(section__iexact='News')
	bio = EditableText.objects.get(section__iexact='Bio')


	context = {'form': form, 'latest_track': latest_track, 'news': news, 'bio': bio, 'mform': mform}
	return render(request, 'home.html', context)

def gallery(request):
	images = GalleryImage.objects.all()
	context = {'images': images}
	return render(request, 'gallery.html', context)

def tracks(request):
	tracks = Track.objects.all().order_by('-date_added')
	context = {'tracks': tracks}
	return render(request, 'music.html', context)
