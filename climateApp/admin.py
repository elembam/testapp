from django.contrib import admin
from .models import DataSource, Resource


# Register your models here.

#class DataSourceAdmin(admin.ModelAdmin):
#    fields = ['name']



admin.site.register(DataSource)
admin.site.register(Resource)
