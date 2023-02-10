from django.db import models

# Create your models here.


class DataSource(models.Model):
    name = models.CharField('Data Source Name',max_length=80)
    registered_country = models.CharField('Country of registration' , max_length=80, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Resource(models.Model):
    TYPE_CHOICES = (
        ('Structural steel and steel profiles','Structural steel and steel profiles'),
        ('Reinforcement for concrete (rebar)','Reinforcement for concrete (rebar)'),
        ('Fresh concrete','Fresh concrete'),
    )
    name = models.CharField('Resource Name',max_length=80)
    producer = models.CharField('Company Name',max_length=80, null=True)
    material = models.CharField('Material Type', max_length=120, choices=TYPE_CHOICES)
    cotwovalue_aonethree = models.FloatField('A1-A3 - Materials (kg CO2e)', )
    cotwovalue_conefour = models.FloatField('C1-C4 - End of life (kg CO2e)', )
    prod_country = models.CharField('Country of production', max_length=80)
    certifier = models.ManyToManyField(DataSource)
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
