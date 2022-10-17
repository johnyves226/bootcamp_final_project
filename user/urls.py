from django.urls import path
from .import  views

urlpatterns=[
     path('',views.index, name='index'),
     path('register/',views.register, name='register'),
     path('photographer_register/',views.photographer_register.as_view(), name='photographer_register'),
     path('viewer_register/',views.viewer_register.as_view(), name='viewer_register'),
     path('login/',views.login_request, name='login'),
     path('logout/',views.logout_view, name='logout'),
]