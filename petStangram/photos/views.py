from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from django.views.generic import UpdateView

from petStangram.common.forms import CommentForm
from petStangram.photos.forms import PhotoAddForm, PhotoEditForm
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

# def photo_edit(request, pk):
#     photo = Photo.objects.get(pk=pk)
#     if request.method == 'POST':
#         form = PhotoEditForm(request.POST, request.FILES, instance=photo)
#         if form.is_valid():
#             form.save()
#             return redirect('photo-details', pk=pk)
#     else:
#         form = PhotoEditForm(instance=photo)
#     context = {
#         'form': form,
#     }
#     return render(request, 'photos/photo-edit-page.html' , context)

class PhotoEditView(UpdateView):
    model = Photo
    form_class = PhotoEditForm
    template_name = 'photos/photo-edit-page.html'
    success_url = reverse_lazy('photo-details')

@login_required
@require_POST
def photo_delete(request, pk):
    photo = get_object_or_404(Photo, pk=pk)

    if request.user.pk != photo.user.pk:
        return HttpResponseForbidden('You are not allowed to delete this photo')

    photo.delete()
    return redirect('home-page')

