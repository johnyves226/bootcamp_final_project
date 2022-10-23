from django.urls import path
from .import views

urlpatterns=[
     path('',views.index, name='event'),
     path('<int:pk>/',views.GetEvent, name='event_detail'),
     path('all/',views.GetAllEvent, name='events_details'),
     path('new/',views.CreateEvent, name='create_event'),
     path('<int:pk>/edit/', views.EventEdit, name='event_edit'),
     path('search/',views.SearchEvent, name='search_event'),
     path('<int:pk>/image/',views.addImages, name='addImages'),
     path('<int:pk>/images/',views.GetEventImage, name='eventImage')


]