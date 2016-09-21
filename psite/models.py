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