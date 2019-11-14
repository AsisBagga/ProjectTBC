from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'events'

urlpatterns=[
    path('', views.view_events, name = 'view_events')
]
