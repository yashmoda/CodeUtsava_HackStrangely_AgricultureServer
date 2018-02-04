"""Agriculture URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin

from Feedback.views import add_feedback, add_complaint
from OTP.views import send_otp, verify_otp
from Products.views import all_product_type, products_type, show_product_details
from Register.views import register_user, login, set_language, add_address, all_address, delete_address
from calculator.views import seed_required
from disease.views import show_disease
from news.views import show_news
from scheme.views import show_all_scheme

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^register/$', register_user),
    url(r'^login/$', login),
    url(r'^set_language/$', set_language),
    url(r'^address/add/$', add_address),
    url(r'^address/all/$', all_address),
    url(r'^address/delete/$', delete_address),
    url(r'^all_product_type/$', all_product_type),
    url(r'^products_type/$', products_type),
    url(r'^show_product_details/$', show_product_details),
    url(r'^seed_required/$', seed_required),
    url(r'^show_disease/$', show_disease),
    url(r'^add_feedback/$', add_feedback),
    url(r'^add_complaint/$', add_complaint),
    url(r'^show_news/$', show_news),
    url(r'^otp/send/$', send_otp),
    url(r'^otp/verify/$', verify_otp),
    url(r'^show_all_scheme/$', show_all_scheme),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)