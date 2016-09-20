from django.shortcuts import render

from .forms import EmailForm


def home_page(request):
	if request.method == 'POST':
		form = EmailForm(request.POST)
		if form.is_valid():
			form.save()
			form = EmailForm()
	else:
		form = EmailForm()


	context = {
		'form': form
	}

	return render(request, 'home.html', context)