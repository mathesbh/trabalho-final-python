from my_app.views import pay_bills_report
from my_app.views.pay_bills import create_pay_bills
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('category/create', views.create_category, name='create_category'),
    path('pay_bills/create', views.create_pay_bills, name='create_pay_bills'),
    path('pay_bills/report', views.pay_bills_report, name='pay_bills_report'),
    path('receive_bills/create', views.create_receive_bills, name='create_receive_bills'),
]