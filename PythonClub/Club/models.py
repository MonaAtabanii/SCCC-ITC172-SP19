from django.db import models 
from django.contrib.auth.models import User

#Meeting
class Meeting(models.Model):
    meetingtitle=models.CharField(max_length=255)
    meetingdate=models.DateField()
    meetingtime=models.TimeField()
    meetinglocation=models.TextField(null=True, blank=True)
    meetingagenda=models.TextField(null=True, blank=True)

    def _str_(self):
        return self.meetingtitle
    
    class Meta:
        db_table = 'meeting'



#Meeting Minutes
class MeetingMinutes(models.Model):
    meetingid = models.ForeignKey(Meeting, on_delete=models.DO_NOTHING) 
    attendance=models.ManyToManyField(User)  
    minutestext=models.TextField(null=True, blank=True)

    def _str_(self):
        return self.minutestext

    class Meta:
        db_table = 'meetingminuts'
            

#Resource
class Resource(models.Model):
    resourcename=models.CharField(max_length=255)
    resourcetype=models.CharField(max_length=255)
    resourceurl=models.URLField(null=True, blank=True)
    dateentered=models.DateField()
    userid=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    resourcedescription=models.TextField(null=True, blank=True)

    def _str_(self):
        return self.resourcename
    
    class Meta:
        db_table='resource'


#Event
class Event(models.Model):
    eventtitle=models.CharField(max_length=255)
    eventlocation=models.TextField(null=True, blank=True)
    eventdate=models.DateField()
    eventtime=models.TimeField()
    userid=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    eventdescription=models.TextField(null=True, blank=True)
    userid=models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def _str_(self):
        return self.eventtitle
    
    class Meta:
        db_table='event'