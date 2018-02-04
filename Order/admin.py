# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
# from Order.models import OrderData, ProductOrderedData
from Order.models import OrderData


class OrderDataAdmin(admin.ModelAdmin):
    list_display = ['user', 'address', 'product', 'quantity', 'amount', 'order_id']
    search_fields = ['user', 'order_id']


admin.site.register(OrderData, OrderDataAdmin)


# admin.site.register(ProductOrderedData, ProductOrderDataAdmin)
