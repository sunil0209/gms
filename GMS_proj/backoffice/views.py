from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth.hashers import make_password,check_password
from shared_model.models import Profile
from user.middleware import auth, login_checker
from shared_model.models import Profile
from shared_model.models import CreateComplaint
from django.http import JsonResponse

from django.contrib.auth.decorators import login_required

def oauth_gmail_login(request):
    # Redirect to Gmail authentication
    return redirect('social:begin', 'google-oauth2')


def oauth_callback(request):
    # Process the callback from the authentication provider
    return redirect('backoffice:dashboard')


# def logout_view(request):
#     # Clear session data
#     request.session.clear()
#     # Redirect to the login page or any other desired page
#     return redirect('login') 

def navigation_admin(request):
    return render(request, 'backoffice/navigation_admin.html')




def dashboard(request):
    User = Profile.objects.all()
    return render(request, 'backoffice/dashboard.html', {'users': User})


# @auth
def profile(request):
    return render(request, 'backoffice/profile.html')
    
def forgot_password(request):
    return render(request, 'backoffice/forgot_password.html')

# @login_checker 
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
                        return redirect("backoffice:dashboard") 
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
            return render(request, 'backoffice/login.html', response_data)

def logout_view(request):
            # Clear session data
            request.session.clear()
            # Redirect to the login page or any other desired page
            return render(request,'backoffice/login.html') 

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
            

            return render(request,'backoffice/registration.html',response_data)
        else:
            return render(request, 'backoffice/registration.html')


def complaint(request, operation,complaint_id = None):
     match operation:
        case 'reply':
            return render(request, 'backoffice/complaint_reply_employee.html')
          
        case 'view':
            print("case view")
            complaint_id=request.GET.get("id")
            print("working id is",complaint_id)
            if complaint_id is not None:
                print("working id is",complaint_id)
                complaints = get_object_or_404(CreateComplaint,id =complaint_id)
                
                profile_id = complaints.profile_id
                print("profile_id",profile_id)
                
                # profile_id=CreateComplaint.objects.get(profile_id=profile_id)
                # p_id=int(complaints.profile_id)
                
                
                profile = Profile.objects.get(id=profile_id)
                print("PROFILE DATA SUCCESS",profile)
                print(type(profile))
                return render(request, 'backoffice/complaint_view.html',{'complaints': complaints,'profile':profile})
            
                
            else:
                complaints = CreateComplaint.objects.all()
                return render(request, 'backoffice/complaint_list.html', {'complaints': complaints})
            
        case 'employee_list':
                employees = Profile.objects.all()
                return render(request, 'backoffice/employee_list.html', {'employees': employees})
        case 'employee_detail':
                employee_id =  request.GET.get('id')
                employees = get_object_or_404(Profile,id =employee_id)
                return render(request, 'backoffice/employee_detail.html',{'employees': employees})


def delete_employee(request,employee_id):
    
    
    # Get the employee object or return 404 if not found
    employee = get_object_or_404(Profile, id=employee_id)
    
    # Delete the employee
    if(employee.delete()):
    
    # Return a JSON response indicating success
        response_data = {
            'status':'success',
            'message':'User deleted successfully',
            'data':[]

        }
    else:
         response_data = {
            'status':'error',
            'message':'Unable to delete user.',
            'data':[]

        }
    return JsonResponse(response_data)