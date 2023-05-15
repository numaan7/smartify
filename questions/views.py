from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import os
from django.contrib.auth  import authenticate,  login, logout
from django.contrib import messages
from taggit.models import Tag 
MESSAGE_TAGS = {
    messages.ERROR:'danger'
}
# Create your views here.
def index(request,tag_slug=None):
    question=Questions.objects.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        questions = questions.filter(tags__in=[tag])
    
    page = request.GET.get('page', 1)

    paginator = Paginator(question, 10)
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)
    
    
   
   
    
    return render(request,"index.html",{ 'questions': questions, 'tag':tag })
def signup(request):
    if request.method=="POST":
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')
        if len(username)<=6:
            messages.error(request, " Your user name must be under 10 characters")
            return redirect('/signup')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('/signup')
        
        myuser = User.objects.create_user(username, email, password)
        myuser.save()
        messages.success(request, " Your Smartify has been successfully created")
        return redirect('/login')
    return render(request,'signup.html')
def loginhandle(request):
    if request.method=="POST":
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username= username, password= password)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("/")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("/login")
    return render(request,'login.html')

def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/')