"""
URL configuration for GMS_proj project.

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
from django.urls import path
from app import views
urlpatterns = [
    path('', views.index, name='index'),
    path('view_all_complaint_admin/', views.view_all_complaint_admin, name='view_all_complaint_admin'),
    path('login/', views.login, name='login'),
    path('view_complaint_reply_user/', views.view_complaint_reply_user, name='view_complaint_reply_user'),
    path('emp_profile_admin/', views.emp_profile_admin, name='emp_profile_admin'),
    path('view_emp_profile_admin/', views.view_emp_profile_admin, name='view_emp_profile_admin'),
    path('specific_complaint/', views.specific_complaint, name='specific_complaint'),
    path('complaint_user/', views.complaint_user, name='complaint_user'),
    path('user_registration/', views.user_registration, name='user_registration'),
    path('profile/', views.profile, name='profile'),
    path('forgot_password',views.forgot_password, name='forgot_password'),
]
