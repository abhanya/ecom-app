from django.urls import path
from . import views

app_name = 'seller'
urlpatterns = [
    path('sellersignup',views.signup,name="s_signup"),
    path('sellerhome',views.home,name="sellerhome"),
]
