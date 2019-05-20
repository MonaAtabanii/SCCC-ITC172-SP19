from django.urls import path
from . import views

#this is a comment
urlpatterns = [
    path('', views.index, name='index'), 
    path('getResources/', views.getResources, name='resources'),
    path('getMeetings/', views.getMeetings, name='meetings'),
    path('getMeetingsDetail/<int:id>',views.getMeetingsDetail, name='detail'),
    path('newResource/', views.newResource, name='newresource'),
    path('newMeeting/', views.newMeeting, name='newmeeting'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]
