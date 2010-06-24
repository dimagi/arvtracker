from django.shortcuts import render_to_response
from datetime import datetime
from helper import *
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

def select_chart(request):
    context = {}
    year = datetime.now().date().year
    years = []
    for i in range(0, 5):
        years.append(year-i)
    context["years"] = years
    charts = ['starting_by_stakeholder', 'percentage_initiations']
    context["charts"] = charts
    return render_to_response('patients/select_chart.html', {'context': context})

def charts(request):
    chart = ''
    if request:
        for item in request.POST.items():
            if item[0] == 'chart':
                chart = item[1]
    if chart == 'starting_by_stakeholder':
        url = get_starting_by_stakeholder(request)
    if chart == 'percentage_initiations':
        url = get_percentage_initiations(request)
    return render_to_response('patients/charts.html', {'url': url})
