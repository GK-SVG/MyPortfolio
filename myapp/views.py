from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return render(request,'myapp/index.html')

def about(request):
    return  render(request,'myapp/about.html')