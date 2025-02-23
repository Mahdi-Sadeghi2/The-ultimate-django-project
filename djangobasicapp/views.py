from django.shortcuts import render, HttpResponse
import datetime
import requests

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
     return(response)

# Getting users details individually in card
def load_user_details(request):

    if request.method == "POST":
        
        #Defining a page counter by getting useridcounter form Html page
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
