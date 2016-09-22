from django.db import models
from django.utils.safestring import mark_safe

class Email(models.Model):
	name = models.CharField(max_length=80)
	email = models.EmailField()

	def __str__(self):
		return '%s - %s' % (self.name, self.email)

class GalleryImage(models.Model):
	picture = models.FileField(upload_to='gallery/')

	def image_tag(self):
		return mark_safe('<img src="%s" width="200" />' % (self.picture.url))

	def __str__(self):
		return '%s' % (self.picture.name, )

	image_tag.short_description = 'Image'

class Collaborator(models.Model):
	role_name = models.CharField(max_length=200)
	personal_url = models.CharField(max_length=150)

	def __str__(self):
		return '%s' % (self.role_name, )

class Track(models.Model):
	track_title = models.CharField(max_length=60, null=True, blank=True)
	soundcloud_html = models.CharField(max_length=500)
	spotify_url = models.CharField(max_length=500)
	youtube_url = models.CharField(max_length=500)
	apple_music_url = models.CharField(max_length=500)
	tidal_url = models.CharField(max_length=500)
	collaborators = models.ManyToManyField(Collaborator)

	date_added = models.DateField(auto_now_add=True)

	def __str__(self):
		return '%s' % (self.track_title, )
