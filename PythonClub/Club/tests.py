from django.test import TestCase
from .models import Event, MeetingMinutes, Meeting, Resource
from datetime import datetime
from django.urls import reverse
from .forms import ResourceForm, MeetingForm
from django.contrib.auth.models import User 


# Create your tests here.

class EventTest(TestCase):

    def test_eventstringOutput(self):
        event=Event(eventtitle='Have Fun')
        self.assertEqual(str(event), event.eventtitle)


    def test_eventtablename(self):
        self.assertCountEqual(str(Event._meta.db_table), 'event')


class MeetingTest(TestCase):

    def test_meetingstringOutput(self):
        meeting=Meeting(meetingtitle='Python Club Weekly Meeting')
        self.assertEqual(str(meeting), meeting.meetingtitle)

    def test_meetingtablename(self):
        self.assertCountEqual(str(Meeting._meta.db_table), 'meeting')


class MeetingMinutesTest(TestCase):

    def test_momstringOutput(self):
        mom=MeetingMinutes(minutestext='not yet implemented')
        self.assertEqual(str(mom), mom.minutestext)

    def test_momtablename(self):
        self.assertCountEqual(str(MeetingMinutes._meta.db_table), 'meetingminuts')


class ResourceTest(TestCase):

    def test_resourcestringOutput(self):
        resource=Resource(resourcename='Python Club')
        self.assertEqual(str(resource), resource.resourcename)

    def test_resourcetablename(self):
        self.assertCountEqual(str(Resource._meta.db_table), 'resource')


#Test Views & Forms
#index
class TestIndex(TestCase):
    
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    #Testing the template index.html    
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Club/index.html')


#getResources
class TestGetResource(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/Club/resources')
        self.assertEqual(response.status_code, 404)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('resources'))
        self.assertEqual(response.status_code, 200)

    #Testing the template resource.html    
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('resources'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Club/resources.html')
 
#newResource check the form
class New_ResourceForm_Test(TestCase):

    def setUp(self):
        self.test_user=User.objects.create_user(username='Mona', password='P@ssw0rd1')
        self.resources_list = Resource.objects.create(resourcename='New Webpage', resourcetype='webpag', resourceurl='http://newwebpage.com', dateentered='2019-05-17', userid=self.test_user, resourcedescription='Good webpage to practice')

    """ # Valid Form Data
    def test_ResourceForm_is_valid(self):
        form = ResourceForm(data={'resourcename': "New Webpage", 'resourcetype': "webpage", 'resourceurl': "http://newwebpage.com", 'dateentered': "2019-05-17", 'userid':self.test_user, 'resourcedescription':"Good webpage to practice" })
        self.assertTrue(form.is_valid()) """
         

    # Invalid Form Data
    def test_ResourceForm_invalid(self):
        form = ResourceForm(data={'resourcename': "New Webpage", 'resourcetype': "webpage", 'resourceurl': "http://newwebpage.com", 'dateentered': "2019-05-17", 'userid':"Mona", 'resourcedescription':"Good webpage to practice" })
        self.assertFalse(form.is_valid()) 

 

#getMeetings
class TestGetMeeing(TestCase):

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/Club/meetings')
        self.assertEqual(response.status_code, 404)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('meetings'))
        self.assertEqual(response.status_code, 200)

    #Testing the template meetings.html    
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('meetings'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Club/meetings.html')


#newMeeting check the form
class New_Meeting_Form_Test(TestCase):      

  # Invalid Form Data
    def test_MeetingForm_invalid(self):
        form = MeetingForm(data={'meetingtitle': "New Meeting", 'meetingdate': "2019-05-17", 'meetingtime': " ", 'meetinglocation': "New Location", 'meetingagenda':"New Agenda" })
        self.assertFalse(form.is_valid())



#getMeetingsDetail
class TestGetMeeingDetails(TestCase):

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/Club/meetingsdetails')
        self.assertEqual(response.status_code, 404) 

        """ def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('detail'))
        self.assertEqual(response.status_code, 200)"""

    """#Testing the template meetingsdetails.html    
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('detail', args=(self.meetdetail_list.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Club/meetingsdetails.html')"""

#loginmessage
class TestLoginMessage(TestCase):

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/Club/loginmessage')
        self.assertEqual(response.status_code, 301)
    
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('loginmessage'))
        self.assertEqual(response.status_code, 200)
    
    #Testing the template loginmessage.html
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('loginmessage'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Club/loginmessage.html')

#logoutmessage
class TestLogoutMessage(TestCase):

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/Club/logoutmessage')
        self.assertEqual(response.status_code, 301)
    
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('logoutmessage'))
        self.assertEqual(response.status_code, 200)

    #Testing the template logoutmessage.html
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('logoutmessage'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Club/logoutmessage.html')


#Testing Templates
#newmeeting.html
class New_meeting_authentication_test(TestCase):
    def setUp(self):
        self.test_user=User.objects.create_user(username='Mona1', password='P@ssw0rd1')
        self.resources_list = Meeting.objects.create(meetingtitle='New Meeting', meetingdate='2019-05-17', meetingtime='10:10:10:00', meetinglocation='New Location', meetingagenda='New Agenda')

    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newmeeting'))
        self.assertRedirects(response, '/accounts/login/?next=/Club/newMeeting/')

    def test_Logged_in_uses_correct_template(self):
        login=self.client.login(username='Mona1', password='P@ssw0rd1')
        response=self.client.get(reverse('newmeeting'))
        self.assertEqual(str(response.context['user']), 'Mona1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Club/newmeeting.html')


#newresource.html
class New_Resource_authentication_test(TestCase):
    def setUp(self):
        self.test_user=User.objects.create_user(username='Mona1', password='P@ssw0rd1')
        self.resources_list = Resource.objects.create(resourcename='New Webpage', resourcetype='webpag', resourceurl='http://newwebpage.com', dateentered='2019-05-17', userid=self.test_user, resourcedescription='Good webpage to practice')

    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newresource'))
        self.assertRedirects(response, '/accounts/login/?next=/Club/newResource/')

    def test_Logged_in_uses_correct_template(self):
        login=self.client.login(username='Mona1', password='P@ssw0rd1')
        response=self.client.get(reverse('newresource'))
        self.assertEqual(str(response.context['user']), 'Mona1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Club/newresource.html')



