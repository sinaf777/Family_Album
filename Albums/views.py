from django.shortcuts import render

# Create your views here.
def album_list(request):
    # Logic for listing albums
    return render(request, 'Albums/album_list.html')

def album_upload(request):
    # Logic for uploading a new album
    return render(request, 'Albums/album_upload.html')

def album_detail(request, pk):
    # Logic for viewing album details
    return render(request, 'Albums/album_detail.html')