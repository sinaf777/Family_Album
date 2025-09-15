from django.shortcuts import render

# Create your views here.
def user_register(request):
    # Logic for user registration
    return render(request, 'Users/register.html')

def user_login(request):
    # Logic for user login
    return render(request, 'Users/login.html')

def user_logout(request):
    # Logic for user logout
    return render(request, 'Users/logout.html')

def user_profile(request):
    # Logic for user profile
    return render(request, 'Users/profile.html')