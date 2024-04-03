app_name = 'user'
from django.contrib import admin
from django.urls import path
from user import views
urlpatterns = [
     path('', views.navigation, name='navigation'),
    path('complaints/<str:operation>/', views.complaint, name='complaints'),
    path('user/<str:operation>/', views.user, name='user'),
    # path('profile/', views.profile, name='profile'),
    # path('forgot_password/',views.forgot_password, name='forgot_password'),
    # path('dashboard_user/',views.dashboard_user, name='dashboard'),
    # path('logout_view/',views.logout_view, name='logout_view'),
    # path('login/', views.login_page, name='login'),
    # path('emp_profile_admin/', views.emp_profile_admin, name='emp_profile_admin'),
    # path('view_emp_profile_admin/', views.view_emp_profile_admin, name='view_emp_profile_admin'),
    # path('view_all_complaint_admin/', views.view_all_complaint_admin, name='view_all_complaint_admin'),
    # path('user_registration/', views.user_registration, name='user_registration'),
]
