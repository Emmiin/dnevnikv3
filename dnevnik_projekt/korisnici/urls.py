from django.urls import path
from . import views

urlpatterns = [    
    path('', views.home, name='korisnici-home'),
    path('about/', views.about, name='korisnici-about')
]