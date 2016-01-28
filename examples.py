#Examples

import requests,json
gtt_access_token = "12345qwerty"
gtt_account_key = "12345"
gtt_training_key = "12345"			#identifier for a training event
gtt_recording_id = "123456"
gtt_registrant_key = "7786065520477863681"
gtt_session_key = "3745519"			#identifier for a session in a training event

#get organizers
organizers = gttGetOrganizers(gtt_access_token,gtt_account_key)
for organizer in organizers:
    print "Details for organizer:",organizer['email']
    for key,value in organizer.iteritems():
        print "\t%-20s: %-30s" % (key,value)

#create training event
gtt_event_details = {
    "name": "Test",
    "description": "Test",
    "timeZone": "GMT",
    "times": [{
            "startDate": "2016-02-27T17:00:00Z",
            "endDate": "2016-02-27T18:00:00Z"
        }],
    "registrationSettings": {
        "disableConfirmationEmail": "true",
        "disableWebRegistration": "true"
    },
    "organizers": [200000000001309446]
}
event = gttCreateTrainingEvent(gtt_access_token,gtt_organizer_key,gtt_event_details)
print "New event training key is: "+str(event)

#get all future training events
events = gttGetTrainingEvents(gtt_access_token,gtt_organizer_key)
for event in events:
    for key,value in event.iteritems():
        print "\t%-20s: %-30s" % (key,value)
    print "------------------------"

#get single training event
event = gttGetTrainingEvent(gtt_access_token,gtt_organizer_key,gtt_training_key)
for key,value in event.iteritems():
    print "\t%-20s: %-30s" % (key,value)

#delete a training event
event = gttDeleteTrainingEvent(gtt_access_token,gtt_organizer_key,gtt_training_key)
​print event

#get management url of a training event
url = gttGetManagementURLForTrainingEvent(gtt_access_token,gtt_organizer_key,gtt_training_key)
print url

#update details of an existing training event
gtt_event_details = {
    "name": "New Name",
    "description": "New Description"
}
update = gttUpdateTrainingEventDetails(gtt_access_token,gtt_organizer_key,gtt_event_details)
print update

#get training event organizers
organizers = gttGetTrainingEventOrganizers(gtt_access_token,gtt_organizer_key,gtt_training_key)
for organizer in organizers:
    for key,value in organizer.iteritems():
        print "\t%-20s: %-30s" % (key,value)

#update training event organizers
organizerchange = gttUpdateTrainingEventOrganizers(gtt_access_token,gtt_organizer_key,gtt_training_key,gtt_event_details)
print organizerchange

#update training event registration settings
gtt_event_details = {
    "disableConfirmationEmail": "true",
    "disableWebRegistration": "true"
}
registration = gttUpdateTrainingEventRegistrationSettings(gtt_access_token,gtt_organizer_key,gtt_training_key,gtt_event_details)
print registration.content
print registration

#get start url for a training event
starturl = gttGetStartURLForTrainingEvent(gtt_access_token,gtt_organizer_key,gtt_training_key)
print starturl
print starturl.content

#start a training event
starturl = gttStartTrainingEvent(gtt_access_token,gtt_organizer_key,gtt_training_key)
for key,value in starturl.iteritems():
    print "\t%-20s: %-30s" % (key,value)

#update training event times
gtt_event_details = {
  "timeZone": "string",
  "times": [
    {
      "startDate": "2016-03-27T17:00:00Z",
      "endDate": "2016-03-27T18:00:00Z"
    }
  ],
  "notifyRegistrants": "true",
  "notifyTrainers": "true"
}
newtimes = gttUpdateTrainingTimes(gtt_access_token,gtt_organizer_key,gtt_training_key,gtt_event_details)
​for key,value in newtimes.iteritems():
    print "\t%-20s: %-30s" % (key,value)

#get recordings for a training event
recordings = gttGetRecordingsForTrainingEvent(gtt_access_token,gtt_organizer_key,gtt_training_key)
for key,value in recordings.iteritems():
    print "\t%-20s: %-30s" % (key,value)
​
#get download url for a recording
recordingurl = gttGetDownloadURLForRecording(gtt_access_token,gtt_training_key,gtt_recording_id)
for key,value in recordingurl.iteritems():
    print "\t%-20s: %-30s" % (key,value)

#Register student for a Training Event
gtt_student_details = {
  "email": "paulsmart101@gmail.com",
  "givenName": "paul",
  "surname": "smart"
}
registration = gttRegisterStudentOnTrainingEvent(gtt_access_token,gtt_organizer_key,gtt_training_key,gtt_student_details)
for key,value in registration.iteritems():
    print "\t%-20s: %-30s" % (key,value)

#Get Training Registrants
registrants = gttGetTrainingEventRegistrants(gtt_access_token,gtt_organizer_key,gtt_training_key)
for registrant in registrants:
    for key,value in registrant.iteritems():
        print "\t%-20s: %-30s" % (key,value)

#Get Training Registrant (single)
registrant = gttGetTrainingEventRegistrant(gtt_access_token,gtt_organizer_key,gtt_training_key,gtt_registrant_key)
for key,value in registrant.iteritems():
    print "\t%-20s: %-30s" % (key,value)
	
#Cancel a Registration
cancelled = gttCancelRegistration(gtt_access_token,gtt_organizer_key,gtt_training_key,gtt_registrant_key)
print cancelled
print cancelled.content

#Get Sessions by Date Range
gtt_date_details = {
  "startDate": "2016-01-25T00:00:00Z",
  "endDate": "2016-01-27T00:00:00Z"
}
sessions = gttGetSessionsByDate(gtt_access_token,gtt_organizer_key,gtt_date_details)
for session in sessions:
    for key,value in session.iteritems():
        print "\t%-20s: %-30s" % (key,value)
    print "------------------"

#Get Attendance Details by Session Key
attendance = gttGetAttendanceBySession(gtt_access_token,gtt_organizer_key,gtt_session_key)
for attend in attendance:
    print attend
    for key,value in attend.iteritems():
        print "\t%-20s: %-30s" % (key,value)
    for intime in attend['inSessionTimes']:
        print "\t------------------"
        for key,value in intime.iteritems():
            print "\t%-20s: %-30s" % (key,value)
    print "------------------------"

#Get Sessions By Training Key
sessions = gttGetSessionsByTrainingKey(gtt_access_token,gtt_organizer_key,gtt_training_key)
for session in sessions:
    for key,value in session.iteritems():
        print "\t%-20s: %-30s" % (key,value)
    print "------------------"
