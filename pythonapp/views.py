from django.shortcuts import render

from pythonapp.models import Family

# Create your views here.


def index(request):
    all_family = Family.objects.all()
    return render(request, 'pythonapp/index.html', {"characters": all_family})
