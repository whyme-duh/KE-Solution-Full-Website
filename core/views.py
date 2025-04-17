from django.shortcuts import render
from . models import Service

# Create your views here.
def index(request):
    services = Service.objects.all()
    return render (request, 'core/home.html', {"services": services})


def llc_view(request):
    return render (request, 'core/LLC/llc.html')