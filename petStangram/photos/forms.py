from django import forms

from petStangram.photos.models import Photo


class PhotoAddForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ('user',)

        labels = {
            'photo': 'Photo',
            'description': 'Description',
            'location': 'Location',
            'tagged_pets': 'Tagged Pets',
        }

