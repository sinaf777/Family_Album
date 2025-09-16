from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Album, Photo
from .forms import AlbumForm, PhotoForm, MultipleUploadPhotoForm
# Create your views here.
@login_required
def album_list(request):
    # Logic for listing albums
    albums = Album.objects.filter(user=request.user)
    return render(request, 'Albums/album_list.html', {'albums': albums})

@login_required
def album_create(request):
    # Logic for creating a new album
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            album = form.save(commit=False)
            album.user = request.user
            album.save()
            return redirect('albums:album_list')
    else:
        form = AlbumForm()
    return render(request, 'Albums/album_form.html', {'form': form})

@login_required
def album_detail(request, pk):
    # Logic for viewing album details
    album = get_object_or_404(Album, pk=pk, user=request.user)
    return render(request, 'Albums/album_detail.html', {'album': album})

@login_required
def photo_upload(request, album_id):
    album = get_object_or_404(Album, id=album_id, user=request.user)

    if request.method == 'POST':
        form = MultipleUploadPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            files = request.FILES.getlist('photos')
            for f in files:
                Photo.objects.create(album=album, image=f)
            return redirect('albums:album_detail', pk=album.id)
    else:
        form = MultipleUploadPhotoForm()

    return render(request, 'Albums/photo_upload.html', {'form': form, 'album': album})