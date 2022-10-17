from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import User,Photographer,Viewer

class PhotographerSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    location = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_photographer = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        photographer = Photographer.objects.create(user=user)
        photographer.phone_number = self.cleaned_data.get('phone_number')
        photographer.location = self.cleaned_data.get('location')
        photographer.save()
        return user

class ViewerSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    designation = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_viewer = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        viewer = Viewer.objects.create(user=user)
        viewer.phone_number = self.cleaned_data.get('phone_number')
        viewer.designation = self.cleaned_data.get('designation')
        viewer.save()
        return user