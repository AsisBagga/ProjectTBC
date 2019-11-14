from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = 'enquiry'

urlpatterns=[
    path('', views.base, name = 'enquiry'),
    path(r'book/', views.book, name = 'bookacomedian'),
    path(r'produce/', views.produce, name = 'produceashow'),
    path(r'thankyou/', views.thankyou, name = 'thankyou')
]
