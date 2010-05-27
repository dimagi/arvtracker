from django.shortcuts import render_to_response
from helper import handle_uploaded_file
from forms import UploadFileForm

def index(request):
    return render_to_response('patients/index.html', {})

def upload(request):
    return render_to_response('patients/upload.html', {})

def uploader(request):
    result = 'Upload failed.'
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            result = 'Upload succeeded.'
    # code for parsing csv file
    return render_to_response('patients/uploader.html', {'result': result})
