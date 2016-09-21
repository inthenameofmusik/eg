from django.contrib import admin

from .models import Email, GalleryImage


class GalleryImageAdmin(admin.ModelAdmin):
	fields = ('image_tag', )
	readonly_fields = ('image_tag', )


admin.site.register(Email)
admin.site.register(GalleryImage, GalleryImageAdmin)