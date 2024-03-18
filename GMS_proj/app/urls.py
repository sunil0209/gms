
from django.contrib import admin
from django.urls import path
from app import views
urlpatterns = [
    path('', views.index, name='index'),
    path('view_all_complaint_admin/', views.view_all_complaint_admin, name='view_all_complaint_admin'),
    path('login/', views.login_page, name='login'),
    path('view_complaint_reply_user/', views.view_complaint_reply_user, name='view_complaint_reply_user'),
    path('emp_profile_admin/', views.emp_profile_admin, name='emp_profile_admin'),
    path('view_emp_profile_admin/', views.view_emp_profile_admin, name='view_emp_profile_admin'),
    path('specific_complaint/', views.specific_complaint, name='specific_complaint'),
    path('complaint_user/', views.complaint_user, name='complaint_user'),
    path('user_registration/', views.profile_original, name='profile_original'),
    path('profile/', views.profile, name='profile'),
    path('forgot_password/',views.forgot_password, name='forgot_password'),
    path('dashboard/',views.dashboard, name='dashboard'),
]
