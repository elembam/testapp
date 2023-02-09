from django.contrib import admin
from .models import DataSource


# Register your models here.

class DataSourceAdmin(admin.ModelAdmin):
    fields = ['name', 'registered_country']

admin.site.register(DataSource, DataSourceAdmin)
