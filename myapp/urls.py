from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='Home'),
    path('about/',views.about,name='About'),
    path('project/',views.project,name='Project'),
    path('certificate/',views.certificate,name='Certificate'),   
]
