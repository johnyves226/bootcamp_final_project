from datetime import datetime
from django import forms
from django.db import transaction
from user.models import User,Photographer,Viewer
from .models import Event


class EventCreateForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ['name','description','is_active','author']
        widgets = {'author': forms.HiddenInput()}
        labels = {
            'name': 'Event Name',
            'description': 'Event Description',
            'is_active':'active event'
        }


class ImageForm(forms.ModelForm):
    event_id = forms.IntegerField(required=False)
    images =  forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}),required=False)
    tags = forms.CharField(max_length=50, required=False)

    class Meta(EventCreateForm.Meta):
        fields = EventCreateForm.Meta.fields + ['images','event_id','tags']