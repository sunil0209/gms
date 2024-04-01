from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth.hashers import make_password,check_password
from shared_model.models import Profile
from user.middleware import auth, login_checker
from shared_model.models import Profile

def logout_view(request):
    # Clear session data
    request.session.clear()
    # Redirect to the login page or any other desired page
    return redirect('login') 

def index(request):
    return render(request, 'index.html')
def view_all_complaint_admin(request):
    return render(request, 'view_all_complaint_admin.html')

@login_checker 
def login_page(request ,response_data=None):
    response_data = {
        'status': '',
        'message': [],
        'data': '',
    }

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = Profile.objects.get(email=email)
            if Profile.objects.filter(email=email).exists() and check_password(password, user.password):
                request.session['is_logged_in'] = True
                request.session['email_id'] = user.email
                request.session['profile_id'] = user.id
                # Check if the provided password matches the hashed password
                # Both email exists and password matches, redirect to dashboard
                return redirect("dashboard") 
            else:
                # User with given email doesn't exist
                request.session['is_logged_in'] = False
                response_data['status'] = 'error'
                response_data['message'] = ['Invalid Credentials Provided']
        except Profile.DoesNotExist:
            request.session['is_logged_in'] = False
            response_data['status'] = 'error'
            response_data['message'] = ['Invalid Credentials Provided']
            # response_data['data'] = request.POST

    return render(request, 'login.html', response_data)

@auth
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
@auth
def profile(request):
    return render(request, 'profile.html')

def home(request):
    
    return render(request, 'home.html')
# def logout_user(request):
#     logout(request)


def forgot_password(request):
    return render(request, 'forgot_password.html')


def admin_registration(request):
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
           

        return render(request,'registration.html',response_data)
    else:
        return render(request, 'registration.html')
        
def view_all_members(request):
    return render(request,"view_all_members.html")

def employee_list(request):
    employees = Profile.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})

def employee_detail(request,employee_id):
    employee_id =  request.GET.get('id')
    employees = get_object_or_404(Profile,id =employee_id)
    return render(request, 'employee_detail.html',{'employees': employees})

   
