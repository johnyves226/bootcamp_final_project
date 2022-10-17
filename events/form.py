from datetime import datetime
from django import forms
from django.db import transaction
from user.models import User,Photographer,Viewer
from .models import Event


class EventCreateForm():
    name = forms.CharField(max_length=200, null=False)
    description = forms.TextField()


    def save(self):

        pass