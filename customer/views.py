from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request,'pages/customerhome.html')

def cart(request):
    return render(request,'pages/cart.html')


def pdetails(request):
    return render(request,'pages/productdetails.html')