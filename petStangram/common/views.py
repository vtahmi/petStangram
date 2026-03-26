from pydoc import resolve

from django.shortcuts import render, redirect, resolve_url
from pyperclip import copy

from petStangram.common.forms import CommentForm
from petStangram.common.models import Like
from petStangram.photos.models import Photo


def home_page(request):
    all_photos = Photo.objects.prefetch_related('tagged_pets').all()
    comment_form = CommentForm()
    context = {
        'all_photos': all_photos,
        'comment_form': comment_form,
    }
    return render(request, 'common/home-page.html', context)


def like(request, photo_id):
    photo = Photo.objects.get(pk=photo_id)
    like_object = Like.objects.filter(to_photo_id=photo_id, user=request.user).first()
    if like_object:
        like_object.delete()
    else:
        Like.objects.create(to_photo_id=photo_id, user=request.user)
    return redirect(request.META.get('HTTP_REFERER') + f'#{photo.id}')

def share_photo(request, photo_id):
    #pip install pyperclip
    # This will copy the URL to the clipboard
    #this is not working on server, only local
    copy(request.META.get('HTTP_HOST') + resolve_url('photo-details', photo_id))
    return redirect(request.META.get('HTTP_REFERER') + f'#{photo_id}')

def add_comment(request, photo_id):
    form = CommentForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        comment = form.save(commit=False)
        comment.to_photo = Photo.objects.get(pk=photo_id)
        comment.user = request.user
        comment.save()
    return redirect(request.META.get('HTTP_REFERER') + f'#{photo_id}')

