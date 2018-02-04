from django.conf.urls import url

from Products.views import all_product_type, show_product_details, products_type

urlpatterns = [
    url(r'^all_types/$', all_product_type),
    url(r'^show_product_details/$', show_product_details),
    url(r'^products_type/$', products_type)
]