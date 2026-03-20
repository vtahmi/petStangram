from django.shortcuts import render

from petStangram.photos.models import Photo


def photo_add(request):
    return render(request, 'photos/photo-add-page.html')

def photo_details(request, pk):
    photo = Photo.objects.get(pk=pk)
    comments = photo.comment_set.all()
    context = {
        'photo': photo,
        'comments': comments,
    }
    return render(request, 'photos/photo-details-page.html', context)

def photo_edit(request, pk):
    return render(request, 'photos/photo-edit-page.html' , {'pk': pk})
