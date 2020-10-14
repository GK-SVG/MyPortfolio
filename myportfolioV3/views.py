from django.shortcuts import render

# Create your views here.
def homeV3(request):
    return render(request,'myportfolioV3/home.html',{'home':'active'})


def services(request):
    return render(request,'myportfolioV3/service.html',{'service':'active'})