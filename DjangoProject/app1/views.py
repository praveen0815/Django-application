from django.shortcuts import render
from django.http import HttpResponse

from app1.models import *

def data(request): 
    data = Student.objects.all()
    return render(request, "home.html", {'d': data})
