from django.urls import path
from . import views

app_name = 'hcart'
urlpatterns = [
    path('login',views.cart_login,name='clogin'),
    path('pass',views.cart_password,name='pass'),
    path('',views.cust_home,name='home'),
    path('custsignup',views.cust_signup,name='signup'),
    path('card',views.card_signup,name='card'),
]
