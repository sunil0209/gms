app_name = 'user'
from django.contrib import admin
from django.urls import path
from user import views
from user.views import oauth_gmail_login, oauth_callback
urlpatterns = [
    path('', views.navigation, name='navigation'),
    path('complaint/<str:operation>/', views.complaint, name='complaints'),
    path('profile/', views.profile, name='profile'),
    path('forgot_password/',views.forgot_password, name='forgot_password'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('logout_view/',views.logout_view, name='logout_view'),
    path('login/', views.login, name='login'),
    path('change_password',views.change_password,name='change_password'),
    path('profile_update/', views.profile_update, name='profile_update'),
    path('registration_user/', views.registration_user, name='registration_user'),
    #Authentication login
    path('oauth/gmail/', oauth_gmail_login, name='oauth_gmail_login'),
    path('oauth/callback/', oauth_callback, name='oauth_callback'),
]
