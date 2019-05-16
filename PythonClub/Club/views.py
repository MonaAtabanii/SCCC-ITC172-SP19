from django.shortcuts import render, get_object_or_404
from .models import Event, MeetingMinutes, Meeting, Resource
#from .forms import ProductForm, ReviewForm


# Create your views here.
def index(request):
    return render(request, 'Club/index.html')

def getResources(request):
    resources_list=Resource.objects.all()
    context={'resources_list' : resources_list }
    return render(request, 'Club/resources.html', context=context)

def getMeetings(request):
    meetings_list=Meeting.objects.all()
    return render(request, 'Club/meetings.html',{'meetings_list' : meetings_list})

def getMeetingsDetail(request, id):
    meetdetail_list=get_object_or_404(Meeting, pk=id)
    #prod=Product.objects.get_object_or_404(Product, pk=id)
    #meetdetail_list=get_object_or_404(Meeting, pk=id)
    #reviewcount=Review.objects.filter(meeting=id).count()
    #reviews=Review.objects.filter(meeting=id)
    context={
         'meetdetail_list' : meetdetail_list,
         #'reviewcount' : reviewcount,
         #'reviews': reviews,
    }
    return render (request, 'Club/meetingsdetails.html', context=context)