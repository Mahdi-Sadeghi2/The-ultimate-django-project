
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse


from django.contrib.auth.forms import (AuthenticationForm,
                                       PasswordChangeForm,
                                       )

from django.contrib.auth import (login, logout, authenticate,
                                 update_session_auth_hash)

from django.contrib.auth.decorators import login_required

from .forms import SignUpForm, ChangeProfileForm


# You need to login to access home page
@login_required
def home(request):
    templatefile = 'order/home.html'
    return render(request, templatefile)


def sign_up(request):
    templatefile = 'order/signup.html'
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, templatefile, {'form': form})


def login_view(request):
    templatefile = 'order/login.html'
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, templatefile, {'form': form})


@login_required
def change_password(request):
    templatefile = 'order/change_password.html'
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('home')
    else:
        form = PasswordChangeForm(request.user)

    return render(request, templatefile, {'form': form})


@login_required
def change_profile(request):
    templatefile = 'order/profile.html'

    # Check if the request method is POST (form submission)
    if request.method == 'POST':
        form = ChangeProfileForm(request.POST, instance=request.user)
        # Validate the form
        if form.is_valid():
            form.save()  # Save the changes to the user profile
            return redirect('home')  # Redirect to a success page

    # If not POST or the form is invalid, instantiate the form with the current user data
    else:
        form = ChangeProfileForm(instance=request.user)

    # Render the template with the form
    return render(request, templatefile, {'form': form})


@login_required
def delete_account(request):
    templatefile = 'order/delete_account.html'
    if request.method == 'POST':
        request.user.delete()
        return redirect('login')
    return render(request, templatefile)


@login_required
def sign_out(request):
        logout(request)
        return redirect('login')
    


# Working with cookies
def cookie_page(request):
    templatefile= "order/cookie.html"
    cookies = request.COOKIES
    return render(request, templatefile, {'cookies':cookies})


# Create cookies
def create_cookies(request):
    if request.method == "POST":
        cookie_name = request.POST.get('cookie_name')
        cookie_value = request.POST.get('cookie_value')
        response = HttpResponseRedirect(reverse('cookie'))
        response.set_cookie(cookie_name, cookie_value,max_age=120)
        return response
    return JsonResponse({'message': 'Invalid request method'})


# Delete all cookies
def clear_cookies(request):
        response = HttpResponseRedirect(reverse('cookie'))
        for key in request.COOKIES:
            response.delete_cookie(key)
        return response


# Read cookies
def read_cookies(request, cookie_name):
        templatefile = 'order/read_cookie.html'
        cookie_value = request.COOKIES.get(cookie_name, None)
        return render(request, templatefile, {'cookie_name': cookie_name, 'cookie_value': cookie_value})


# Delete one cookie
def delete_cookie(request, cookie_name):
    response = HttpResponseRedirect(reverse('cookie'))
    response.delete_cookie(cookie_name)
    return response



# Working with sessions
def session_page(request):
    templatefile = 'order/session_data.html'
    sessiont_data = request.session.items()
    return render(request,templatefile, {'session_data': sessiont_data})


# Add session
def add_session(request):
    if request.method == 'POST':
        session_key = request.POST.get('session_key')
        session_value = request.POST.get('session_value')
        request.session[session_key] = session_value
        response = HttpResponseRedirect(reverse('session_data'))
        return response
    return JsonResponse({'message': 'Invalid request method'})


# Clear all sessions
def clear_sessions(request):
    request.session.flush()
    respose = HttpResponseRedirect(reverse('session_data'))
    return respose


# Read one sessions
def read_sessions(request,session_key):
    templatefile = 'order/read_session.html'
    session_value= request.session.get(session_key, None)
    return render(request, templatefile, {'session_key':session_key, 'session_value':session_value})


# Delete one session
def delete_session(request,session_key):
    templatefile = 'order/delete_session.html'
    if session_key in request.session:
        respose = HttpResponseRedirect(reverse('session_data'))
        del request.session[session_key]
        return respose
    else:
        return JsonResponse({'message': 'Sesssion not found'})