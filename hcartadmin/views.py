from django.shortcuts import render

# Create your views here.

def adhome(request):
    return render(request,'pages/adminhome.html')

def approve(request):
    return render(request,'pages/approveseller.html')

def viewcust(request):
    return render(request,'pages/viewcust.html')

def viewseller(request):
    return render(request,'pages/viewseller.html')