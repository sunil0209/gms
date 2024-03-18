from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth.hashers import make_password 
from .models import Profile
from django.contrib.auth import login


from django.contrib.auth.models import User


from django.contrib import messages

from django.contrib.auth import authenticate
from .models import UserRegistration

# def list_all_user(request):
    
    
#     return render(request, 'index.html')


def index(request):
    return render(request, 'index.html')
def view_all_complaint_admin(request):
    return render(request, 'view_all_complaint_admin.html')

def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:  # Corrected variable name from 'User' to 'user'
            login(request, user)
            return redirect('dashboard')  # Redirect to dashboard on successful login
        else:
            print("error")
            messages.error(request, 'Invalid username or password')
            return redirect('login')  # Redirect to login page if authentication fails
    return render(request, 'login.html')
    # if request.method == 'POST':
    #     email = request.POST.get('email')
    #     password = request.POST.get('password')

    #     if  not User.objects.filter(email = email ).exists():
    #         messages.error(request,"invalid username")
            
        
    #     user = authenticate(email = email, password = password)

    #     if user is None:
    #         messages.error (request,'Invalid Password')
    #         return redirect('login')
    #     else:
    #         login(request,user)
    #         return redirect('dashboard')
    # return render(request, 'login.html')
        


    # if request.method == 'POST':
    #     form = AuthenticationForm(data=request.POST)
    #     if form.is_valid():
    #         user = form.get_user()
    #         login(request, user)
    #         return redirect('dashboard')  # Redirect to home page after successful login
    # else:
    #     form = AuthenticationForm()
    # return render(request, 'login.html', {'form': form})

def dashboard(request):
    User = Profile.objects.all()
    return render(request, 'dashboard.html', {'users': User})
   
   
  
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
def profile(request):
    return render(request, 'profile.html')

def home(request):
    
    return render(request, 'home.html')

def forgot_password(request):
    return render(request, 'forgot_password.html')


def profile_original(request):
    if request.method == 'POST':

        name = request.POST.get('name','')
        mobile = request.POST.get('mobile','')
        email = request.POST.get('email','')
        password = request.POST.get('password','')
        confirm_password = request.POST.get('confirm_password','')
    

        error_msg = []

        response_data = {
            'status':'',
            'message':[],
            'data':''
        }
        

        if name == '':
            error_msg.append('Field Name cannot be Empty.')
        if email == '':
            error_msg.append('Field Email cannot be Empty.')
        if mobile == '':
            error_msg.append('Field Mobile Number cannot be Empty.')
        if password == '':
            error_msg.append('Field Password cannot be Empty.')
        if confirm_password == '':
            error_msg.append('Field Confirm Password cannot be Empty.')

        try:
            validate_email(email)
        except ValidationError as e:
            error_msg.append('Invalid Email Provided')
        else:
            pass

        if len(mobile) != 10:
            error_msg.append('Mobile number must be 10 character in length.')

        if password != confirm_password:
            error_msg.append('Password donot match confirm password.') 

        if Profile.objects.filter(email=email).exists():
                error_msg.append('Email already exists. Please use a different email address.')
                
        if(len(error_msg) == 0):
            response_data['status'] = 'success'
            response_data['message'] = ['User Registered Successfully.']
            response_data['data'] = []
            hashed_password=make_password(password)
            # If the email doesn't exist, create a new Profile object
            user = Profile.objects.create(name=name, mobile=mobile, email=email, password=hashed_password)
        else:
            response_data['status'] = 'error'
            response_data['message'] = error_msg
            response_data['data'] = request.POST
           

        return render(request,'profile_original.html',response_data)
    else:
        return render(request, 'profile_original.html')
        