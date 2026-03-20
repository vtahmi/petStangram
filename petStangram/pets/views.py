from django.shortcuts import render, redirect

from petStangram.pets.forms import PetCreateForm, PetDeleteForm
from petStangram.pets.models import Pet


def pet_details(request, username:str, pet_slug:str):
    pet = Pet.objects.get(slug=pet_slug)
    all_photos = pet.photo_set.prefetch_related('tagged_pets').all()
    context = {
        'pet': pet,
        'all_photos': all_photos,
    }
    return render(request, 'pets/pet-details-page.html', context)

def pet_add(request):
    form = PetCreateForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('profile-details', pk=1)  # TODO change to current user's profile pk
    context = {
        'form': form,}
    return render(request, 'pets/pet-add-page.html', context)

def pet_edit(request, username:str, pet_slug:str):
    pet = Pet.objects.get(slug=pet_slug)
    form = PetCreateForm(request.POST or None, instance=pet)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('pet-details', username=username, pet_slug=pet_slug)
    context = {
        'pet': pet,
        'form': form,
    }
    return render(request, 'pets/pet-edit-page.html', context)

def pet_delete(request, username:str, pet_slug:str):
    pet = Pet.objects.get(slug=pet_slug)
    form = PetDeleteForm(instance=pet)
    if request.method == 'POST':
        pet.delete()
        return redirect('profile-details', pk=1)  # TODO change to current user's profile pk
    context = {
        'pet': pet,
        'form': form,
    }
    return render(request, 'pets/pet-delete-page.html', context)

