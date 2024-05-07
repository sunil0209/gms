# # from functools import wraps
# # from django.shortcuts import redirect

# # def wrapper(view_func):
# #     @login_auth(view_func)
# #     def decorated_view(request, *args, **kwargs):
# #         if not request.user.is_authenticated:
# #             return redirect("login")  # Redirect to the login page if the user is not authenticated
# #         else:
# #             return view_func(request, *args, **kwargs)
# #     return decorated_view

# from functools import wraps
# from django.shortcuts import redirect

# def unauthenticated_user(view_func):
#     @login_auth(view_func)
#     def wrapper(request, *args, **kwargs):
#         if request.user.is_authenticated:
#             return redirect("index")  # Redirect to the index page if the user is already authenticated
#         else:
#             return view_func(request, *args, **kwargs)
#     return wrapper

from django.shortcuts import render,redirect



def auth_b(view_function):
    def wrapped_view(request, *args, **kwargs):
        print("case 2 auth_b")
        print("session:",request.session.items())
        if 'is_logged_in' not in request.session:
              request.session['is_logged_in'] = False
              return redirect('backoffice:login')
        else:
             if request.session['is_logged_in'] == False:   
                return redirect('backoffice:login')
        

        return view_function(request, *args, **kwargs)
    return wrapped_view

def login_checker_b(view_function):
    def wrapped_view(request, *args, **kwargs):
        print('case 1')
        if 'is_logged_in' in request.session:
            if request.session['is_logged_in'] == True :
                return redirect('backoffice:dashboard')
            
      
        return view_function(request, *args, **kwargs)
    return wrapped_view

