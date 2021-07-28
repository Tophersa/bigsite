from django.shortcuts import render
from django.http import HttpResponse
from general.models import Featured

# Create your views here.

def index(request):
    fea = Featured.objects.all()
    page1 = Featured.objects.get(pageNumber = "1")
    page2 = Featured.objects.get(pageNumber = "2")
    page3 = Featured.objects.get(pageNumber = "3")

    context = {
        'page1': page1,
        'page2': page2,
        'page3': page3,
        'fea': fea
    }
    return render(request, 'general/index.html', context)
