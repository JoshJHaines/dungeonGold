from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User
import datetime

# Create your views here.
def index(request):
    # return HttpResponse("It's Working so far")
    return render(request, "gateway.html")

def register(request):
    print("#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#")
    print(request.POST)
    resultFromValidator = User.objects.registerValidator(request.POST)
    print("*******Errors from Login********")
    print(resultFromValidator)
    if len(resultFromValidator) > 0:
        for key,value in resultFromValidator.items():
            messages.error(request, value)
        return redirect("/")
    newUser = User.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'],password=request.POST['password'])
    request.session['loggedInId'] = newUser.id
    return redirect("/home")

def login(request):
    print("#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#")
    print(request.POST)
    resultFromValidator = User.objects.loginValidator(request.POST)
    print("*******Errors from Login********")
    print(resultFromValidator)
    if len(resultFromValidator) > 0:
        for key,value in resultFromValidator.items():
            messages.error(request, value)
        return redirect("/")
    emailMatch = User.objects.filter(email=request.POST['email'])
    request.session['loggedInId'] = emailMatch[0].id
    return redirect("/home")

def home(request):
    loggedInUser = User.objects.get(id=request.session['loggedInId'])
    # travelors = Destination.objects.filter(travelors = loggedInUser)
    
    # notjoined = Destination.objects.exclude(travelors = loggedInUser)
    context = {
        'loggedInUser':loggedInUser,
        # "allDest": Destination.objects.all(),
        # 'travelors': travelors,
        # 'notjoined': notjoined
    }
    # return HttpResponse("It's Working so far")
    return render(request, "home.html", context)

def logout(request):
    request.session.clear()
    return redirect("/") 

def newCamp(request):
    loggedInUser = User.objects.get(id=request.session['loggedInId'])
    context = {
        'loggedInUser':loggedInUser
    }
    return render(request, "newCamp.html", context) 

def newChar(request):
    loggedInUser = User.objects.get(id=request.session['loggedInId'])
    context = {
        'loggedInUser':loggedInUser
    }
    return render(request, "newChar.html", context)