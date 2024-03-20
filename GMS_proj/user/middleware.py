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



def auth(view_function):
    def wrapped_view(request, *args, **kwargs):
    
        if request.session['is_logged_in'] == False:
            return redirect('login')
        return view_function(request, *args, **kwargs)
    return wrapped_view

