from contextlib import redirect_stderr
from email.message import Message
from pyexpat.errors import messages
from django.shortcuts import render

from django.shortcuts import render , redirect
from .models import Profile , Meep
from django.contrib import messages
from django.contrib.auth import authenticate , login, logout
# Create your views here.

def home(request):
    if request.user.is_authenticated:
        meeps = Meep.objects.all().order_by("-created_at")
    return render (request, "home.html", {"meeps"})


def profile_list(request):
    if request.user.is_authenticated:

        profiles = Profile.objects.exclude(user = request.user)
        return render(request, "profile_list.html", {"profile":profiles})
    else:
        messages.succes(request , ("you must be logged in to view this page"))
        return redirect("home")


def profile(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)
        
        meep = Meep.objects.filter(user_id = pk)
    
       

        if request.method == "POST":
            #get user 
            current_user_profile = request.user.profile

            action = request.POST["follow"]
            #decide to follow or un
            if action == "unfollow":
                curent_user_profile.follows.remove(profile)
            elif action == "follow"  :
                current_user_profile.follows.add(profile)
            #save profile
            curent_user_profile.save()

        return render ( request, "profile.html", {"profile":profile , "meep":Meep} )
        
    else:
         messages.succes(request , ("you must be logged in to view this page"))
         return redirect("home") 



def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request , username = username , password = password)
        if user is not None : 
            login(request, user)
            messages.succes(request, ("You have been loged in "))
            return redirect("home")

        else:  
            messages.succes(request, ("there was an error logging in "))
            return redirect("login")  
        

    else:    
        return render( request, "login.html", {} )

def logout_user(request):
    logout(request)
    messages.succes(request, (" you have been loged out, sorry to see you go "))
    return redirect('home')
