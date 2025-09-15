from django.shortcuts import render

# Create your views here.
def photo_list(request):
    # Logic for listing photos
    return render(request, 'Photos/photo_list.html')

def photo_upload(request):
    # Logic for uploading a new photo
    return render(request, 'Photos/photo_upload.html')

def photo_detail(request, pk):
    # Logic for viewing photo details
    return render(request, 'Photos/photo_detail.html')