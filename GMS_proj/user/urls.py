app_name = 'user'
from django.contrib import admin
from django.urls import path
from user import views
urlpatterns = [
    path('', views.navigation, name='navigation'),
    path('complaint/<str:operation>/', views.complaint, name='complaints'),
    #path('<str:operation>/', views.user, name='user'),
    path('profile/', views.profile, name='profile'),
    path('forgot_password/',views.forgot_password, name='forgot_password'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('logout_view/',views.logout_view, name='logout_view'),
    path('login/', views.login, name='login'),
    # path('emp_profile_admin/', views.emp_profile_admin, name='emp_profile_admin'),
    # path('view_emp_profile_admin/', views.view_emp_profile_admin, name='view_emp_profile_admin'),
    # path('view_all_complaint_admin/', views.view_all_complaint_admin, name='view_all_complaint_admin'),
    path('registration_user/', views.registration_user, name='registration_user'),
]
