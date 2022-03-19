from django.shortcuts import render
from django.http import HttpResponse


def fb(request):
    return render(request,'fb.html')
    

# Create your views here.
