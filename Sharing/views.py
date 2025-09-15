from django.shortcuts import render

# Create your views here.
def sharing_list(request):
    # Logic for listing shared items
    return render(request, 'Sharing/sharing_list.html')

def sharing_upload(request):
    # Logic for uploading a new shared item
    return render(request, 'Sharing/sharing_upload.html')

def sharing_detail(request, pk):
    # Logic for viewing shared item details
    return render(request, 'Sharing/sharing_detail.html')