from django.shortcuts import render
from .models import DataSource
# Create your views here.


def data_sources(request):
    list_sources = DataSource.objects.all()
    return render(request, 'climateApp/source_list.html', {
        'list_sources': list_sources,
    })

def home(request):
    name = "Name"
    return render(request,
        'climateApp/home.html', {
        "name": name,
    })