from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm, LoginForm
# Create your views here.

def auth_view(request):
    login_form = LoginForm()
    signup_form = SignUpForm()
    message = ''

    if request.method == 'POST':
        if 'login' in request.POST:
            login_form = LoginForm(request, data=request.POST)
            if login_form.is_valid():
                user = login_form.get_user()
                login(request, user)
                return redirect('users:dashboard')
            else:
                message = 'Login failed. Check username or password.'
        elif 'signup' in request.POST:
            signup_form = SignUpForm(request.POST)
            if signup_form.is_valid():
                user = signup_form.save(commit=False)
                user.set_password(signup_form.cleaned_data['password'])
                user.save()
                login(request, user)
                return redirect('users:dashboard')
            else:
                message = 'Sign up failed. Check the fields.'

    return render(request, 'users/auth.html', {
        'login_form': login_form,
        'signup_form': signup_form,
        'message': message
    })
    
@login_required
def dashboard_view(request):
    return render(request, 'users/dashboard.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('users:auth')