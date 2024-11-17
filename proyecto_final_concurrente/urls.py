"""
URL configuration for proyecto_final_concurrente project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from supercomputer import views

urlpatterns = [
    path('supercomputers/', views.supercomputer_list, name='supercomputer_list'),   
    path('add/',views.add_supercomputer, name='add_supercomputer'),
    path('edit/<int:pk>/',views.edit_supercomputer, name='edit_supercomputer'),
    path('delete/<int:pk>/',views.delete_supercomputer, name='delete_supercomputer'),
]
