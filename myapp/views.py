from django.shortcuts import render,HttpResponse
from .models import *
import json
from django.http import JsonResponse
# Create your views here.
def home(request):
    mycv = MyCV.objects.all()[0]
    return render(request,'myapp/index.html',{'mycv':mycv})

def about(request):
    mycv = MyCV.objects.all()[0]
    skills=Skill.objects.all()
    return  render(request,'myapp/about.html',{'skills':skills,'mycv':mycv})

def project(request):
    mycv = MyCV.objects.all()[0]
    projects=Project.objects.all()
    return render(request,'myapp/project.html',{'projects':projects,'mycv':mycv})

def certificate(request):
    mycv = MyCV.objects.all()[0]
    certificates=Certificate.objects.all()
    return render(request,'myapp/certificate.html',{'certificates':certificates,'mycv':mycv})
