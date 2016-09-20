from django.db import models

class Email(models.Model):
	name = models.CharField(max_length=80)
	email = models.EmailField()

	def __str__(self):
		return '%s - %s' % (self.name, self.email)

class GalleryImage(models.Model):
	picture = models.FileField(upload_to='gallery/')