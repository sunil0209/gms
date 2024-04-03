
app_name = 'backoffice'
from django.contrib import admin
from django.urls import path
from backoffice import views
# from user import views as user_views
urlpatterns = [
    path('', views.navigation, name='navigation'),
    path('complaints/<str:operation>/', views.complaint, name='complaints'),
    path('backoffice/<str:operation>/', views.backoffice, name='backoffice'),

    
    # path('complaint_list/', views.complaint_list, name='complaint_list'),
    # path('complaint_view/', views.complaint_view, name='complaint_view'),
    # path('admin_registration/', views.admin_registration, name='admin_registration'),
    # path('profile/', views.profile, name='profile'),
    # path('employee_detail/', views.employee_detail, name='employee_detail'),
    # path('dashboard_admin/',views.dashboard, name='dashboard'),
    # path('login/',views.login_page, name='login'),
    # path('logout_view/',views.logout_view, name='logout_view'),
    # path('employee_list/',views.employee_list, name='employee_list'),
    
    # # path('view_all_members/',views.view_all_members, name='view_all_members'),
    # path('employee_detail/<int:employee_id>/', views.employee_detail, name='employee_detail'),
    # path('view_all_complaint_admin/', views.view_all_complaint_admin, name='view_all_complaint_admin'),
    # path('view_complaint_reply_user/', views.view_complaint_reply_user, name='view_complaint_reply_user'),
    #path('emp_profile_admin/', views.emp_profile_admin, name='emp_profile_admin'),
    # path('view_emp_profile_admin/', views.view_emp_profile_admin, name='view_emp_profile_admin'),
    # path('specific_complaint/', views.specific_complaint, name='specific_complaint'),
    # path('forgot_password/',views.forgot_password, name='forgot_password'),
]
