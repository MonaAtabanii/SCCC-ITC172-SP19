from django.contrib import admin
from .models import Meeting, MeetingMinutes, Resource, Event

# Register the models 
admin.site.register(Meeting)
admin.site.register(MeetingMinutes)
admin.site.register(Resource)
admin.site.register(Event)