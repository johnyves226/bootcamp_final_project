from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView
from django.template import loader
from django.contrib import messages
from django.db.models import Q
from events.form import EventCreateForm, ImageForm
from events.models import Event, Image
from user.models import Photographer


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


@login_required
class SearchPhotographer(ListView):
    model = Photographer
    template_name = "../templates/result.html"

    def get_queryset(self):
        query = self.request.GET.get('q')
        queryset = Photographer.objects.filter(
            Q(user__first_name__icontains=query) | Q(user__last_name__icontains=query) | Q(user__user_name__icontains=query)
            | Q(user__email__icontains=query)
        ).distinct()
        return queryset

@login_required
def showImage(request,pke, pk):
    template = loader.get_template('../templates/showImage.html')
    event = Event.objects.get(pk=pke)
    image=Image.objects.get(pk=pk)
    context = {'event': event,'image':image}
    return HttpResponse(template.render(context, request))

@login_required
def EventEdit(request, pk):
     pass


@login_required
def GetEvent(request,pk):
      template = loader.get_template('../templates/event_details.html')
      event = Event.objects.get(pk=pk)
      context = {'event':event}
      return HttpResponse(template.render(context, request))


@login_required
def GetEventImage(request,pk):
    template = loader.get_template('../templates/events_images_view.html')
    event = Event.objects.get(pk=pk)
    images=Image.objects.filter(event=event)
    context = {'event':event,'images':images}
    return HttpResponse(template.render(context, request))

@login_required
def GetAllEvent(request):
    template = loader.get_template('../templates/events_view.html')
    events = Event.objects.filter(author=request.user)
    context = {'event':events}
    return HttpResponse(template.render(context, request))



@login_required
def addImages(request,pk):
    template = loader.get_template('../templates/events_images_view.html')
    if request.method == 'POST':
        form = ImageForm(request.POST or None, request.FILES or None)
        images = request.FILES.getlist('images')
        event = Event.objects.get(pk=pk)
        for image in images:
            print("for file valid ")
            Image.objects.create(images=image,event=event)
            print("create image ok ")
        images = Image.objects.filter(event=event)
        context = {'event':event,'images': images}
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponse('/')


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
