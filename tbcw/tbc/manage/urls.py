from django.conf.urls import url
from django.urls import path
from . import views

app_name = "manage"

urlpatterns=[
    path('',views.manage, name = "manage"),
    path('host_event/', views.host_event, name="host_event"),
    path('comedian_profile/', views.comedian_profile, name="comedian_profile"),
    path('fetch_comedian/<int:pk>/', views.fetch_comedian, name="fetch_comedian"),
    path('approve_comedian/<int:pk>/', views.approve_comedian, name="approve_comedian"),
    path('reject_comedian/<int:pk>/', views.reject_comedian, name="reject_comedian")
]
