from django.urls import path
from . import views

urlpatterns = [
    path('', views.start, name='clubs-start'),
    path('home/', views.home, name='clubs-home'),
    path('explore/', views.explore, name='clubs-explore'),
    path('clubs/', views.clubs, name='clubs-my_clubs'),
    
]
