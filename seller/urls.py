from django.urls import path
from . import views

app_name = 'seller'
urlpatterns = [
    path('sellerhome',views.home,name="sellerhome"),
    path('addproduct',views.addpro,name="addproduct"),
    path('catlog',views.catlog,name="catlog"),
    path('sellpassword',views.sellpassword,name="sellpassword"),
]
