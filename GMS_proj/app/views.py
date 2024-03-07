from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import JsonResponse
from django.http import HttpResponse
def index(request):
    return render(request, 'index.html')
def view_all_complaint_admin(request):
    return render(request, 'view_all_complaint_admin.html')
def login(request):
    return render(request, 'login.html')
def view_complaint_reply_user(request):
    return render(request, 'view_complaint_reply_user.html')
def emp_profile_admin(request):
    return render(request, 'emp_profile_admin.html')
def view_emp_profile_admin(request):
    return render(request, 'view_emp_profile_admin.html')
def specific_complaint(request):
    return render(request, 'specific_complaint.html')
def complaint_user(request):
    return render(request, 'complaint_user.html')
# def user_registration(request):
#     if request.method == 'POST':
#         name=request.POST.get('name')
#         mobile=request.POST.get('mobile')
#         email=request.POST.get('email')
#         password=request.POST.get('password')
#         confirm_password=request.POST.get('confirm_password')
        
#         #VALIDATION 
#         if not name or not mobile or not email or not password or not confirm_password:
#             messages.error(request, 'All fields are required.')
#             return redirect('user_registration.html')
#         if password != confirm_password:
#             messages.error(request, 'Password and Confirm Password do not match')
#             return redirect('user_registration.html')
 
#         #IF SUCCESS
#         messages.success(request, 'Registration successful!')
#         return redirect('home')  # Redirect to a success page

#     return render(request, 'user_registration.html')
# Create your views here.
def home(request):
    return render(request, 'home.html')

from django.http import HttpResponse


def user_registration(request):
    if request.method == 'POST':
        # Handle form data and perform validation here
        # Replace this with your actual form processing logic

        # Example: Get form data
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

         #VALIDATION 
        if not name or not mobile or not email or not password or not confirm_password:
            messages.error(request, 'All fields are required.')
            return redirect('user_registration')
        if password != confirm_password:
            messages.error(request, 'Password and Confirm Password do not match')
            return redirect('user_registration')
 
        #IF SUCCESS
        messages.success(request, 'Registration successful!')
        return redirect('home')  # Redirect to a success page

    return render(request, 'user_registration.html')



def xhr_user_registration(request):
   
    if request.method == 'POST':
        name=request.POST.get('name')
        mobile=request.POST.get('mobile')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        
        #VALIDATION 
        if not name or not mobile or not email or not password or not confirm_password:
            return JsonResponse({'status':'error','message':'empty','data':[]})
        if password != confirm_password:
            return JsonResponse({'status':'error','message':'password issue','data':[]})
    else:
         return JsonResponse({'status':'error','message':'Invalid request type','data':[]})
        
 