from django.shortcuts import render_to_response
from helper import handle_uploaded_file
from forms import UploadFileForm
from models import Patient

def index(request):
    return render_to_response('patients/index.html', {})

def upload(request):
    return render_to_response('patients/upload.html', {})

def uploader(request):
    result = 'Upload failed.'
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            result = handle_uploaded_file(request.FILES['file'])
    return render_to_response('patients/uploader.html', {'result': result})

def data(request):
    patients = Patient.objects.all()
    return render_to_response('patients/data.html', {'patients': patients})
