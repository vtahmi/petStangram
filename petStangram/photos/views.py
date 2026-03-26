from django.shortcuts import render, redirect

from petStangram.common.forms import CommentForm
from petStangram.photos.forms import PhotoAddForm
from petStangram.photos.models import Photo


def photo_add(request):
    if request.method == 'POST':
        form = PhotoAddForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = request.user
            photo.save()
            form.save_m2m()
            return redirect('home-page')

    else:
        form = PhotoAddForm()
    return render(request, 'photos/photo-add-page.html', {'form': form})

def photo_details(request, pk):
    photo = Photo.objects.get(pk=pk)
    comments = photo.comment_set.all()
    comment_form = CommentForm()
    context = {
        'photo': photo,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'photos/photo-details-page.html', context)

def photo_edit(request, pk):
    return render(request, 'photos/photo-edit-page.html' , {'pk': pk})
