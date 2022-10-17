from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views import View
from django.template import loader

from events.form import EventCreateForm


@login_required
class CreateEvent(View):
    context = {}
    def get(self, request):
        template = loader.get_template('../templates/create_event.html')
        form = EventCreateForm()
        self.context['form'] = form
        return HttpResponse(template.render(self.context, request))