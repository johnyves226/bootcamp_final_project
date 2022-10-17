from django.contrib import admin
from .models import User, Photographer, Viewer

admin.site.register(User)
admin.site.register(Photographer)
admin.site.register(Viewer)

