from django.shortcuts import render,HttpResponse
from .models import *
# Create your views here.
def home(request):
    return render(request,'myapp/index.html')

def about(request):
    skills=Skill.objects.all()
    return  render(request,'myapp/about.html',{'skills':skills})

def project(request):
    projects=Project.objects.all()
    return render(request,'myapp/project.html',{'projects':projects})

def certificate(request):
    certificates=Certificate.objects.all()
    return render(request,'myapp/certificate.html',{'certificates':certificates})
