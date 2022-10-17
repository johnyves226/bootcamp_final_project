from django.urls import path
from .import views

urlpatterns=[
     path('create_event/',views.CreateEvent, name='create_event'),
]