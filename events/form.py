from datetime import datetime
from django import forms
from django.db import transaction
from user.models import User,Photographer,Viewer
from .models import Event


class EventCreateForm():
    # name = forms.CharField(max_length=200, null=False)
    # description = forms.TextField()
    # is_active = forms.BooleanField(default=False)

    class Meta:
        model = Event
        model = ('name','description','is_active')
        labels = {
            'name': 'Display Name'
        }

