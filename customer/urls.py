from django.urls import path
from . import views

app_name = 'customer'
urlpatterns = [
    path('custhome',views.homepage,name='chome'),
    path('cart',views.cart,name='cart'),
    path('productdet',views.pdetails,name='product'),
]
