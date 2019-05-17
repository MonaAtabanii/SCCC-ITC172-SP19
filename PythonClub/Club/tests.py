from django.test import TestCase
from .models import Event, MeetingMinutes, Meeting, Resource

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
