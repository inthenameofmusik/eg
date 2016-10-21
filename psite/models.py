from django.db import models
from django.utils.safestring import mark_safe

import os

class Register(models.Model):
	name = models.CharField(max_length=80)
	email = models.EmailField()

	def save(self, *args, **kwargs):
		email = 'echo "Name: %s\n\nEmail: %s" | mail -s "New Signup!" pomuzaxix@hostcalls.com' % (self.name, self.email )
		os.system(email)
		# super(Register, self).save(*args, **kwargs)
		models.Model.save(self, *args, **kwargs)

	def __str__(self):
		return '%s - %s' % (self.name, self.email)

class Message(models.Model):
	"""contacting Elena via a message"""
	mfrom = models.EmailField()
	msubject = models.CharField(max_length=60)
	mcontent = models.TextField()

	def save(self, *args, **kwargs):
		email = 'echo "From: %s\n\nMessage: %s" | mail -s "%s" pomuzaxix@hostcalls.com' % (self.mfrom, self.mcontent, self.msubject )
		os.system(email)
		super(Message, self).save(*args, **kwargs)

	def __str__(self):
		return '%s - %s' % (self.mfrom, self.msubject)
		

class GalleryImage(models.Model):
	picture = models.FileField(upload_to='gallery/')

	def image_tag(self):
		return mark_safe('<img src="%s" width="200" />' % (self.picture.url))

	def __str__(self):
		return '%s' % (self.picture.name, )

	image_tag.short_description = 'Image'

	class Meta:
		verbose_name='Gallery Image'
		verbose_name_plural='Galllery Images'

class Collaborator(models.Model):
	role_name = models.CharField(max_length=200)
	personal_url = models.CharField(max_length=150)

	def __str__(self):
		return '%s' % (self.role_name, )

class Track(models.Model):
	track_title = models.CharField(max_length=60, null=True, blank=True)
	soundcloud_html = models.CharField('SoundCloud HTML', max_length=500)
	spotify_url = models.CharField('Spotify URL', max_length=500)
	spotify_html = models.CharField('Spotify HTML', max_length=600)
	youtube_url = models.CharField('YouTube URL', max_length=500)
	apple_music_url = models.CharField('Apple Music URL', max_length=500)
	apple_music_html = models.CharField('Apple Music HTML', max_length=700)
	tidal_url = models.CharField('Tidal URL', max_length=500)
	collaborators = models.ManyToManyField(Collaborator)

	date_added = models.DateField(auto_now_add=True)

	def __str__(self):
		return '%s' % (self.track_title, )

	class Meta:
		ordering = ['-date_added']

class EditableText(models.Model):
	section = models.CharField(max_length=40, unique=True, editable=False)
	title = models.CharField(max_length=70, null=True, blank=True)
	content = models.TextField(null=True, blank=True)

	def __str__(self):
		return '%s' % (self.section)

	class Meta:
		verbose_name = 'Editable Text'
		verbose_name_plural = 'Editable Text Sections'
