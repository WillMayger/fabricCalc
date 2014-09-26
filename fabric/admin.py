from django.contrib import admin
from fabric.models import CostPerMonth
from fabric.models import Resource
from fabric.models import Product

class CostPerMonthInline(admin.StackedInline):
    model = CostPerMonth
    extra = 3

class ResourceInLine(admin.StackedInline):
    model = Product.resource.through

class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        ('Description', {'fields': ['description'], 'classes': ['collapse']}),
    ]
    inlines = [ResourceInLine]

class ResourceAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        ('Description', {'fields': ['description'], 'classes': ['collapse']}),
    ]

    inlines = [CostPerMonthInline]

admin.site.register(Product, ProductAdmin)
admin.site.register(Resource, ResourceAdmin)