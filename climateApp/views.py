from django.shortcuts import render
from .models import DataSource, Resource
from datetime import datetime
# Create your views here.


def data_sources(request):
    list_sources = DataSource.objects.all()
    return render(request, 'climateApp/source_list.html', {
        'list_sources': list_sources,
    })

def material_list(request):
    materials = Resource.objects.all()
    return render(request, 'climateApp/materials.html', {
        'materials': materials,
    })


def home(request):
    name = "Name"
    now = datetime.now()
    day = now.strftime('%j')
    week = now.strftime('%W')
    zone = now.strftime('%Z')
    month = now.strftime('%B')
    year = now.strftime('%G')
    time = now.strftime('%H:%M:%S.%f')

    return render(request,
        'climateApp/home.html', {
        "name": name,
        "day": day,
        "week": week,
        "month": month,
        "year": year,
        "time": time,
        "zone": zone,

    })


