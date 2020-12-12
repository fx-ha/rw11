from django.contrib import admin

from apps.event.models import Event, Image


class ImageInline(admin.TabularInline):
    model = Image
    extra = 1

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'startdate', 'enddate')
    list_filter = ('startdate', 'enddate')

    inlines = [ImageInline]

admin.site.register(Event, EventAdmin)