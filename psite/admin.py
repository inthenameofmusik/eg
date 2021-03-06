from django.contrib import admin

from .models import Register, GalleryImage, Collaborator, Track, EditableText, Message


class GalleryImageAdmin(admin.ModelAdmin):
	fields = ('image_tag', 'picture')
	readonly_fields = ('image_tag', )

class EdtiableTextAdmin(admin.ModelAdmin):
	fields = ('section', 'title', 'content')
	readonly_fields = ('section', )

	class Media:
		js = [
			'/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
			'/static/js/tinymce_setup.js'
		]

class MessageAdmin(admin.ModelAdmin):
	readonly_fields = ('mfrom', 'msubject', 'mcontent')


admin.site.register(Register)
admin.site.register(GalleryImage, GalleryImageAdmin)
admin.site.register(Collaborator)
admin.site.register(Track)
admin.site.register(EditableText, EdtiableTextAdmin)
admin.site.register(Message, MessageAdmin)