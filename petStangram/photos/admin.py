from django.contrib import admin

from petStangram.photos.models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_of_publication', 'description', 'pets_list')

    def pets_list(self, obj):
        return ", ".join([pet.name for pet in obj.tagged_pets.all()])

