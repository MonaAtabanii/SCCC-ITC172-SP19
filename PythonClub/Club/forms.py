from django import forms 
from .models import Event, MeetingMinutes, Meeting, Resource

class ResourceForm (forms.ModelForm):
    class Meta:
        model=Resource
        fields = '__all__'


class MeetingForm(forms.ModelForm):
    class Meta:
        model=Meeting
        fields = '__all__'

