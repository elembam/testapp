import django_filters
from django_filters import CharFilter
from .models import *

class ResourceFilter(django_filters.FilterSet):
    cotwo_filter = CharFilter(field_name='cotwovalue_aonethree', lookup_expr='lte')
    producer_filter = CharFilter(field_name='producer', lookup_expr='icontains')

    class Meta:
        model = Resource
        fields = '__all__'
        exclude = ['name','producer', 'cotwovalue_conefour' , 'cotwovalue_aonethree' , 'material', 'certifier', 'prod_country']

