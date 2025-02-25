from django.shortcuts import render, HttpResponse, redirect
import datetime
import requests
from django.db import models
from django.core.paginator import Paginator, PageNotAnInteger
from django.conf import settings

from .models import Employee
from .forms import EmployeeForm, UserRegistrationForm
from .templatetags import filters

# Create your views here.


def home(request):
    return HttpResponse('<h1>Hello there!</h1>')


def more_messages(request):
    return HttpResponse('<h1>Hello there!</h1><h1>Hello there!</h1><h2>Hello there!</h2><h3>Hello there!</h3><h4>Hello there!</h4><h5>Hello there!</h5><h6>Hello there!</h6>')


def use_variables_ass_resppnse(request):
    message = "<h1>This is first message</h1>"
    message += "<h2>This is second message</h1>"
    message += "<h3>This is third message</h3>"
    message += "<h4>This is fourth message</h4>"
    message += "<h5>This is fifth message</h5>"
    message += "<h6>This is sixth message</h6>"
    return HttpResponse(message)


def get_request_variables(request):

    message = ''
    if request.method == "GET":
        if request.GET.get('message'):
            message = request.GET.get('message')
        else:
            message = "<h1>You haven't supplied value for message parameter...</h1>"
    # return HttpResponse(message)

    if request.method == "GET":
        if request.GET.get('country'):
            message += request.GET.get('country')
        else:
            message += "<h1>You haven't supplied value for country parameter...</h1>"
    return HttpResponse(message)


def show_time(request):
    todaydate = datetime.datetime.now()
    today = datetime.date.today()
    context = {'today': today, 'todaydate': todaydate}
    return render(request, 'djangobasicapp/showtime.html', context)


def if_tag_demo(request):
    data = {'name': 'Me', 'isvisible': True, 'loggein': False, 'country': 'Ir',
            'workexperience': 5, 'age': 24, 'programmar': True, "handsome": True}
    template_name = 'djangobasicapp/tag.html'
    return render(request, template_name, data)


def show_products(request):
    processors = [
        {'Category': 'AMD', 'processors': [
            'Ryzen 3990', 'Ryzen 3970', 'Ryzen 3960', 'Ryzen 3950']},
        {'Category': 'Intel', 'processors': [
            'Xeon 8362', 'Xeon 8358', 'Xeon 8380']}
    ]
    TemplateFile = 'djangobasicapp/showproduct.html'
    dict = {"processors": processors}
    return render(request, TemplateFile, dict)

# GEtting API for user info from website


def call_restapi():
    BASE_URL = 'https://fakestoreapi.com'
    response = requests.get(f"{BASE_URL}/users")
    return (response)


def index(request):
    return render(request, 'djangobasicapp/index.html')


# Loading captured API and access to data
def load_users2(request):
    templatefilename = "djangobasicapp/showuserscart.html"
    images = 'https://i.pravatar.cc'
    response = call_restapi()
    context = {"users": response.json(), "images": images}
    return render(request, templatefilename, context)


def call_rest_api2(user_id):
    BASE_URL = 'https://fakestoreapi.com'
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    return (response)

# Getting users details individually in card


def load_user_details(request):

    if request.method == "POST":

        # Defining a page counter by getting useridcounter form Html page
        counter = int(request.POST.get("useridcounter"))

        # A next botton to prevnextious user card
        if (request.POST.get("btnNext")):
            counter = counter+1
            if counter >= 11:
                counter = 1

        # A pervious botton to previous user card
        elif (request.POST.get("btnPrevious")):
            counter = counter - 1
            if counter == 0:
                counter = 1

    else:
        counter = 1

    templatefilename = "djangobasicapp/userdetail.html"
    # Calling API crawler form website
    response = call_rest_api2(counter)
    # Calling image crawler from website
    images = 'https://i.pravatar.cc'
    # Gathering info and image in a dictionary
    context = {"user": response.json(), "images": images}
    return render(request, templatefilename, context)


class Authors(models.Model):
    def __init__(self, author_name, country, book_name):
        self.author_name = author_name
        self.country = country
        self.book_name = book_name


def pass_model(request):
    object = Authors("chadman", "USA", "UFC")
    templatfilename = 'djangobasicapp/passmodel.html'
    context = {"Author": object}
    return render(request, templatfilename, context)


# Working with filters
def buitlt_in_filters(request):
    processors = [
        {"name": "Ryzen 3970", "cores": 32},
        {"name": "Ryzen 3950", "cores": 16},
        {"name": "Ryzen 3990", "cores": 64},
    ]
    context = {
        "ProbationPeriod": 4,
        "FirstName": "Connors",
        "LastName": "McGregor",
        "PayForFight": 123456,
        "FirstQuarter": ["Jan", "Feb", "Mar"],
        "SecondQuarter": ["Apr", "May", "Jun"],
        "FQuarter": [1, 2, 3],
        "SQuarter": [4, 5, 6],
        "AboutMe": "i'am Notorious and I'am Ruthless too!",
        "now": datetime.datetime.now(),
        "PreviousFight": "",
        "NextFight": None,
        "Processors": processors,
        "Message": "<h1>I am using escape</h1>",
        "WebSite": "https://www.uiacademy.co.in"
    }
    return render(request, "djangobasicapp/filters.html", context)


# Custom filter
def custom_filter(request):
    web_frameworks = {'Description': 'Django is a python framework that makes it easier to create dynamic web site',
                      'InDemand': '4.8', 'PollNumber': 57650}
    return render(request, 'djangobasicapp/customfilters.html', web_frameworks)

# Working with static files


def test_static(request):
    return render(request, 'djangobasicapp/teststatic.html')


# Getting data from model
def employee_list(request):
    employee = Employee.objects.all()
    templatefile = "djangobasicapp/access.html"
    context = {"Employees": employee}
    return render(request, templatefile, context)


# Using queries for access to more info
def employee_details(request, id):
    employee = Employee.objects.get(id=id)
    templatefile = "djangobasicapp/details.html"
    context = {"Employees": employee}
    return render(request, templatefile, context)


# Deleting employees individually
def employee_delete(request, id):
    employee = Employee.objects.get(id=id)
    templatefile = "djangobasicapp/delete.html"
    context = {"Employees": employee}
    if request.method == "POST":
        employee.delete()
        # Pass neme of the ulr to redirect()
        return redirect('list')
    return render(request, templatefile, context)


# Update employees data
def employee_update(request, id):
    # Getting data from database and making an object
    employee = Employee.objects.get(id=id)
    templatefile = "djangobasicapp/update.html"

    # Add employee object as instance to form to put info in it
    form = EmployeeForm(instance=employee)

    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            # Redirect to the list after saving
            return redirect('list')

    context = {"form": form}
    return render(request, templatefile, context)


# Create new employee data
def employee_insert(request):
    templatefile = "djangobasicapp/create.html"
    form = EmployeeForm()
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        # Pass neme of the ulr to redirect()
        return redirect('list')
    context = {'form': form}
    return render(request, templatefile, context)


# User Signup
def signup(request):
    templatefile = "djangobasicapp/signup.html"
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            print("form validations are successful")
            form.save()
            return redirect('list')
    else:
        form = UserRegistrationForm()

    return render(request, templatefile, {"form": form})


# Implementing pagination
def page(request):
    templatefile = "djangobasicapp/pagination.html"
    # How many item must be in a page
    page_size = int(request.GET.get(
        'page_size', getattr(settings, 'PAGE_SIZE', 5)))
    # Current page
    page = request.GET.get('page', 1)
    employee = Employee.objects.all()
    paginator = Paginator(employee, page_size)
    try:
        employee_page = paginator.page(page)
    except PageNotAnInteger:
        employee_page = paginator.page(1)
    return render(request, templatefile, {'employees_page': employee_page, 'page_size':page_size})
