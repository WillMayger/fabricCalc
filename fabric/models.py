from django.db import models

class Resource(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    def __unicode__(self):
        return self.name

class AdditionalResource(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    def __unicode__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    additionalResource = models.ManyToManyField(AdditionalResource)
    resource = models.ManyToManyField(Resource)

    def __unicode__(self):
        return self.name

class CostPerMonth(models.Model):
    resource = models.ForeignKey(Resource)
    lengthInMonths = models.IntegerField()
    costPerMonth = models.DecimalField(max_digits=16, decimal_places=2)

class AdditionalCostPerMonth(models.Model):
    additionalResource = models.ForeignKey(AdditionalResource)
    lengthInMonths = models.IntegerField()
    costPerMonth = models.DecimalField(max_digits=16, decimal_places=2)