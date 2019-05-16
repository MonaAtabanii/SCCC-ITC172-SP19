from django.shortcuts import render
from .models import Event, MeetingMinutes, Meeting, Resource
#from .forms import ProductForm, ReviewForm


# Create your views here.
def index(request):
    return render(request, 'Club/index.html')

def getResources(request):
    resources_list=Resource.objects.all()
    context={'resources_list' : resources_list }
    return render(request, 'Club/resources.html', context=context)