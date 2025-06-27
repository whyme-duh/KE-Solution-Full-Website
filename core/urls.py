from django.urls import path
from . views import index, llc_view, invoice_bookkeeping_view, services_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name ='index'),
    path('services/', services_view, name ='services'),
    path('llc/', llc_view, name ='llc_view'),
    path('bookkeeping/',invoice_bookkeeping_view, name ='invoice_bookkeeping')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
