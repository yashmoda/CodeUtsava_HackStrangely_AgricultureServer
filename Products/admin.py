# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from Products.models import ProductTypeData, ProductData, ProductImage


class ProductTypeDataAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_type_eng', 'product_type_hi']
    search_fields = ['id']
    
    
admin.site.register(ProductTypeData, ProductTypeDataAdmin)


class ProductDataAdmin(admin.ModelAdmin):
    list_display = ['product_type', 'name_eng', 'name_hindi', 'price']
    search_fields = ['id']
    
    
admin.site.register(ProductData, ProductDataAdmin)
admin.site.register(ProductImage)
