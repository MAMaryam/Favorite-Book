from django.urls import path
from . import views 

urlpatterns =[
    path('', views.index),
    path('register', views.register),
    path('logout', views.logout),
    path('addbooks', views.addbooks),
    path('login', views.login)
]