"""
URL configuration for proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from app1 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('complaint/create/', views.create_complaint, name='create_complaint'),
    path('complaint/list/', views.complaint_list, name='complaint_list'),
    path('complaint/update/<int:complaint_id>/', views.update_complaint, name='update_complaint'),
    path('complaint/delete/<int:complaint_id>/', views.delete_complaint, name='delete_complaint'),
]
