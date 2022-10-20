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


@login_required
def GetEvent(request,pk):
      template = loader.get_template('../templates/event_details.html')
      event = Event.objects.get(pk=pk)
      context = {'event':event}
      return HttpResponse(template.render(context, request))

@login_required
def GetAllEvent(request):
    template = loader.get_template('../templates/events_view.html')
    events = Event.objects.filter(author=request.user)
    context = {'event':events}
    return HttpResponse(template.render(context, request))



@login_required
def addImages(request,pk):
    print("done ")
    template = loader.get_template('../templates/events_view.html')
    if request.method == 'POST':
        form = ImageForm(request.POST or None, request.FILES or None)
        files = request.FILES.getlist('images')
        print("First post if ok")
        if form.is_valid():
            print("if valid ok")
            event = Event.objects.get(pk=pk)
        for f in files:
            print("for file valid ")
            form=Image.objects.create(images=f,event=event)
            img_obj = form.instance
            print("create image ok ")
            context = {'form':form,'img_obj': img_obj}
            return HttpResponseRedirect(template.render(context, request))
        else:
            print("Form invalid, see below error msg")
            print(form.errors)
    else:
        print("Last else")
        form = ImageForm()
        context = {'form':form}
    return HttpResponseRedirect(template.render(context, request))


@login_required()
class SearchEvent(ListView):
    """Class to render search results"""
    model = Event
    template_name = "../templates/event_details.html"

    def get_queryset(self):
        query = self.request.GET.get('q')
        queryset = Event.objects.filter(
            Q(name__icontains=query) | Q(tags__name__icontains=query)
        ).distinct()
        return queryset
