from django.shortcuts import render

# Create your views here.

def cart_login(request):
    return render(request,'pages/clogin.html')
    
def cart_password(request):
    return render(request,'pages/password.html')
def cust_home(request):
    return render(request,'pages/custhome.html')

def cust_signup(request):
    return render(request,'pages/cust_signup.html')

def card_signup(request):
    return render(request,'pages/signupcard.html')