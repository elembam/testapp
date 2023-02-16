from django.forms import ModelForm
from .models import *

class ResourceForm(ModelForm):
    class Meta:
        model = Resource
        fields = '__all__'
