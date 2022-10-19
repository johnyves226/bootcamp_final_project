from django.contrib import admin
from events.models import Event, Image, Tag

admin.site.register(Image)

class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)} # new

admin.site.register(Event, EventAdmin)

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)} # new

admin.site.register(Tag, TagAdmin)


