from django.shortcuts import render

# Create your views here.


def signup(request):
    return render(request,'pages/s_signup.html')


def home(request):
    return render(request,'pages/sellerhome.html')