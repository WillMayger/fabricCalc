from django.contrib import admin
from fabric.models import CostPerMonth
from fabric.models import Resource
from fabric.models import Product
from fabric.models import AdditionalResource
from fabric.models import AdditionalCostPerMonth

class CostPerMonthInline(admin.StackedInline):
    model = CostPerMonth
    extra = 3

class AdditionalCostPerMonthInline(admin.StackedInline):
    model = AdditionalCostPerMonth
    extra = 3

class ResourceInLine(admin.StackedInline):
    model = Product.resource.through

class AdditionalResourceInLine(admin.StackedInline):
    model = Product.additionalResource.through

class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        ('Description', {'fields': ['description'], 'classes': ['collapse']}),
    ]
    inlines = [ResourceInLine, AdditionalResourceInLine]

class ResourceAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        ('Description', {'fields': ['description'], 'classes': ['collapse']}),
    ]

    inlines = [CostPerMonthInline]

class AdditionalResourceAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        ('Description', {'fields': ['description'], 'classes': ['collapse']}),
    ]

    inlines = [AdditionalCostPerMonthInline]


admin.site.register(Product, ProductAdmin)
admin.site.register(Resource, ResourceAdmin)
admin.site.register(AdditionalResource, AdditionalResourceAdmin)