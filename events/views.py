from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView
from django.views import View
from django.template import loader
from requests import request
from django.contrib import messages
from django.db.models import Q
from events.form import EventCreateForm, ImageForm
from events.models import Event, Image


@login_required
def CreateEvent(request):
     context = {}
     template = loader.get_template('../templates/create_event.html')
     if request.method == "POST":
          form = EventCreateForm(request.POST, request.FILES)
          if form.is_valid():
               event=form.save()
               messages.success(request, ('Your event was successfully create!'))
               return redirect('event_detail',pk=event.pk)
          else:
               messages.error(request, 'Error saving form')

          return redirect("/")
     else:
          form=EventCreateForm(initial={'author': request.user})
          events = Event.objects.all()
          context['form'] = form
          context['evensts'] = events
          return HttpResponse(template.render(context, request))


def index():
     pass


def SearchEvent():
     pass


def EventEdit(request, pk):
     pass

def GetEvent(request,pk):
      context = {}
      template = loader.get_template('../templates/event_details.html')
      event = Event.objects.get(pk=pk)
      context['event'] = event
      return HttpResponse(template.render(context, request))



@login_required
def addImages(request,pk):
    context = {}
    template = loader.get_template('../templates/events_view.html')
    form = ImageForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        files = request.FILES.getlist('images')
        if form.is_valid():
            event = Event.objects.get(pk=pk)
        for f in files:
            Image.objects.create(event=event, image=f)
        else:
            print("Form invalid, see below error msg")
            print(form.errors)
    else:
        form = ImageForm()
    return HttpResponseRedirect('/')


@login_required()
class SearchEvent(ListView):
    """Class to render search results"""
    model = Event
    template_name = "../templates/index.html"

    def get_queryset(self):
        query = self.request.GET.get('q')
        queryset = Event.objects.filter(
            Q(title__icontains=query) | Q(tags__name__icontains=query)
            # | Q(text__icontains=query) # will not work bcoz of encryption
        ).distinct()
        return queryset
