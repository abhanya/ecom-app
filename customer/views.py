from django.shortcuts import render,redirect
from seller.models import Product
from hcart.models import Customer
from customer.models import Cart,Wishlist,Oreder
from .auth_gaurd import auth_customer
from django.db.models import Q,F
import random
from django.http import JsonResponse


# Create your views here.

@auth_customer
def homepage_master(request):
    if request.method=='POST':

        customer = Customer.objects.get(id = request.session['customer'])

        customer_name = request.POST['c_name']
        email_address = request.POST['c_email']
        address = request.POST['c_address']
        phone_number = request.POST['c_number']
        gender = request.POST['c_gender']
         

        customer.customer_name = customer_name
        customer.customer_email = email_address
        customer.address = address
        customer.cust_phone = phone_number
        customer.gender = gender
        
        customer.save()
    
    return redirect('customer:customerhome')

def custhom(request):
    product = Product.objects.values('id','product_name','product_image')
    print(product)
    customername = Customer.objects.get(id=request.session['customer'])
    context = {
        'prods':product,
        'cusdata':customername,
        } 
    return render(request,'pages/home_page.html',context)

def whishlist(request):
    wishlist = Wishlist.objects.filter(cust = request.session['customer'])
 
    context ={
        'wish_list':wishlist,
    }
    return render(request,'pages/wishlist.html',context)

@auth_customer
def cart(request):
    product_cart = Cart.objects.filter(cust = request.session['customer']).annotate(total_price = F('prod__product_price')*F('prod_quantity'))
    context ={
        'cart_list':product_cart,
    }
    return render(request,'pages/cart.html',context)

@auth_customer
def pdetails(request,pid):
    msg = ''
    
    product_details = Product.objects.get(id = pid)

    if request.method == 'POST':
        qty = request.POST['qty']

        product_exist = Cart.objects.filter(prod = pid,cust =request.session['customer']).exists()

        if not product_exist:  
            
            cart = Cart(cust_id = request.session['customer'],prod_id = pid)
            cart.prod_quantity = qty
            cart.save()
            return redirect('customer:cart')
        else:
            msg ='already in cart'

    context = {
            'pdetail':product_details,
            'msg':msg
        }
    return render(request,'pages/productdetails.html',context)
       


def addtowishlist(request,pid):
    msg = ""
    product_details = Product.objects.get(id = pid)
    product_exist = Wishlist.objects.filter(prod = pid,cust =request.session['customer']).exists()

    if not product_exist:                        
            wish = Wishlist(cust_id = request.session['customer'],prod_id = pid)
            wish.save()
    else:
        msg ='already in wishlist'

    context = {
            'pdetail':product_details,
            'msg':msg
        }
    return render(request,'pages/productdetails.html',context)

def custpass(request):
    msg =''
    customer_data = Customer.objects.get(id=request.session['customer'])
    if request.method == 'POST':
        customer = Customer.objects.get(id = request.session['customer'])

        current_pass = request.POST['current_pass'] 
        new_pass = request.POST['new_pass'] 
        confirm_pass = request.POST['confirm_pass']

        if customer.cust_pass == current_pass:

            if new_pass == confirm_pass:
                 customer.cust_pass = new_pass
                 customer.save()
                 msg = 'Password changed succesfully'

            else:
                msg = 'Password does not match'

        else:
            msg = 'Incorrect Password'
    context =  {'msg':msg,
                'data': customer_data,
                }
    return render(request,'pages/custpassword.html',context)

def custprof(request):
    msg=''
    customername = Customer.objects.get(id=request.session['customer'])  

    if request.method=='POST':
        customer = Customer.objects.get(id = request.session['customer'])

        customer_name = request.POST['c_name']
        email_address = request.POST['c_email']
        address = request.POST['c_address']
        phone_number = request.POST['c_number']
        gender = request.POST['c_gender']
        propic = request.POST['cust_img']

        customer.customer_name = customer_name
        customer.customer_email = email_address
        customer.address = address
        customer.cust_phone = phone_number
        customer.gender = gender
        customer.cust_pic = propic
        customer.save()
        msg = 'Profile updated successfully'
    context = {
        'cusdata':customername,
        'msg':msg
        }
    return render(request,'pages/custprofile.html',context)

def remove_item(request,pid):
    cart_item = Cart.objects.get(prod = pid,cust = request.session['customer'])
    cart_item.delete()
    return redirect('customer:cart')

def removefromwishlist(request,pid):
    wish_item = Wishlist.objects.get(prod = pid,cust = request.session['customer'])
    wish_item.delete()
    return redirect('customer:wishlist')

def c_logout(request):
    del request.session['customer'] 
    request.session.flush()
    return redirect('hcart:clogin')


def search_prod(request):
    if request.method=='POST':
        search_word = request.POST['searchdata']
        searchproducts = Product.objects.filter(Q(product_name__icontains = search_word) | 
                                                Q(product_details__icontains = search_word) |                                                
                                                Q(product_price__icontains = search_word) |
                                                Q(product_category__icontains = search_word), )

        return render(request,'pages/searchproduct.html',{'searchprod':searchproducts})
                  
    else:
            return redirect('customer:customerhome')

def custcat(request,data=None):
    if data == None:
        products = Product.objects.all()
    elif data == 'newcollections' or  data == 'Crafts' or data == 'home' or data == 'jwelry' or data == 'toy' or data == 'gift':
        products = Product.objects.filter(product_category = data)
    return render(request,'pages/custcatg.html',{'prods':products})
def bestof(request):
    return render(request,'pages/bestof.html')

def totalprice(request):
    qty = request.POST['qty']
    pid = request.POST['pid']

    product = Product.objects.filter(id = pid).values('product_price')
    print(product)

    total = int(qty) * product[0]['product_price']

    print(total)

    return JsonResponse({'total':total})

def quantity(request):
    if request.method =='POST':
        prod_id = int(request.post.get('product_id'))
        if(Cart.objects.filter(cust_id=request.session['customer'],prod_id=prod_id)):
            prod_qty = int(request.POST.get('product_qty'))
            cart = Cart.objects.get(
                cust_id=request.session['customer'],prod_id=prod_id)
            cart.prod_quantity = prod_qty
            cart.save()
            return JsonResponse({'success':True})
            
def checkout(request):
    cart_products = Cart.objects.filter(cust=request.session['customer'])
    totalprice = 100
    for item in cart_products :
        totalprice = totalprice + item.prod.product_price * item.prod_quantity
    if request.method == 'POST':
        new_oreder = Oreder()
        new_oreder.cust = Customer.objects.get(id=request.session['customer'])
        new_oreder.first_name = request.POST.get('fname')
        new_oreder.second_name = request.POST.get('sname')
        new_oreder.address = request.POST.get('address')
        new_oreder.email = request.POST.get('email')
        new_oreder.phone = request.POST.get('phone')
        new_oreder.state = request.POST.get('state')
        new_oreder.city = request.POST.get('city')
        new_oreder.pin = request.POST.get('pin')
        new_oreder.payment_mode = request.POST.get('payment_mode')

        cart = Cart.objects.filter(cust = request.session['customer'])
        cart_totalprice = 100
        for item in cart :
            cart_totalprice = cart_totalprice + item.prod.product_price * item.prod_quantity
        new_oreder.total_price = cart_totalprice
        tracking_no = 'hcrt'+str(random.randint(111111,999999))
        while Oreder.objects.filter(tracking_no = tracking_no) is None:
            tracking_no = 'hcrt'+str(random.randint(111111,999999))
        new_oreder.tracking_no = tracking_no
        new_oreder.save()

    context={
        'cart':cart_products,
        'totalprice':totalprice
    }

    return render(request,'pages/checkout.html',context)

def orderpage(request):
    return render(request,'pages/myorders.html')
