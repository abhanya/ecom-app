from django.shortcuts import render

# Create your views here.



def home(request):
    return render(request,'pages/sellerhome.html')

def addpro(request):
    return render(request,'pages/addprod.html')

def catlog(request):
    return render(request,'pages/catlog.html')

def sellpassword(request):
    return render(request,'pages/spassword.html')