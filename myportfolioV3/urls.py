from django.urls import path
from . import views

urlpatterns = [
    path('',views.homeV3,name='HomeV3'),
    path('services/',views.services,name='Services')
]
