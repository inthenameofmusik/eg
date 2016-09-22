from django.contrib import admin

from .models import Email, GalleryImage, Collaborator, Track


class GalleryImageAdmin(admin.ModelAdmin):
	fields = ('image_tag', 'picture')
	readonly_fields = ('image_tag', )


admin.site.register(Email)
admin.site.register(GalleryImage, GalleryImageAdmin)
admin.site.register(Collaborator)
admin.site.register(Track)