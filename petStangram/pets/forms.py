from django import forms

from petStangram.common.mixins import ReadOnlyMixins
from petStangram.pets.models import Pet


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'date_of_birth', 'personal_photo']
        labels = {
            'name': 'Pet Name',
            'date_of_birth': 'Date of Birth',
            'personal_photo': 'Link to Image',
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter pet name'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'personal_photo': forms.URLInput(attrs={'placeholder': 'Enter link to image'}),
        }
class PetCreateForm(PetForm):
    pass
class PetEditForm(PetForm):
    pass
class PetDeleteForm(ReadOnlyMixins, PetForm):
    pass