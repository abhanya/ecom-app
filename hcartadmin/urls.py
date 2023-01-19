from django.urls import path
from . import views

app_name = 'hcartadmin'

urlpatterns = [
    path('admin',views.adhome,name='adhome'),
    path('approve',views.approve,name='approve'),
    path('viewcust',views.viewcust,name='viewcust'),
    path('viewseller',views.viewseller,name='viewseller'),
]
