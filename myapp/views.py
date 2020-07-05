from django.shortcuts import render,HttpResponse
from .models import *
import json
from django.http import JsonResponse
# Create your views here.
def home(request):
    return render(request,'myapp/index.html')

def about(request):
    skills=Skill.objects.all()
    dict_data={'skills':skills}
    print(dict_data)
    r=json.dumps(dict_data)
    print(r)
    return  JsonResponse(r)

def project(request):
    projects=Project.objects.all()
    return render(request,'myapp/project.html',{'projects':projects})

def certificate(request):
    certificates=Certificate.objects.all()
    return render(request,'myapp/certificate.html',{'certificates':certificates})
