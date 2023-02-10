from django.db import models

# Create your models here.


class DataSource(models.Model):
    name = models.CharField('Data Source Name',max_length=80)
    registered_country = models.CharField(max_length=80)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


