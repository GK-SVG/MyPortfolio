from django.shortcuts import render,HttpResponse
from .models import *
import json
from django.http import JsonResponse
# Create your views here.
def home(request):
    mycv = MyCV.objects.all()[0]
    skills=Skill.objects.all()
    projects=Project.objects.all()
    certificates=Certificate.objects.all()
    return render(request,'myapp/index.html',{'mycv':mycv,'skills':skills,'projects':projects,'certificates':certificates})

