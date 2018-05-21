"""
Your module description
"""
import requests,json
baseurl = "https://api.getgo.com/G2T/rest/"
gtt_access_token = "#############"
gtt_account_key = "#############"
gtt_organizer_key = '#############'

#gtt_training_key = "12345"			#identifier for a training event
#gtt_recording_id = "123456"
#gtt_registrant_key = "7786065520477863681"
#gtt_session_key = "3745519"			#identifier for a session in a training event

def gttGetOrganizers(gtt_access_token,gtt_account_key):
    '''Get organizers for an account
    Requires Access Token and Account Key
    Returns list of dictionaries, one per organizer'''
    gtt_url = baseurl+'accounts/'+gtt_account_key+'/organizers'
    gtt_auth = "OAuth oauth_token="+gtt_access_token
    gtt_headers = {'Content-type':'application/json','Accept':'application/json','authorization':gtt_auth}
    r = requests.get(gtt_url,headers=gtt_headers)
    return r.json()
def gttCreateTrainingEvent(gtt_access_token,gtt_organizer_key,gtt_event_details):
    '''Schedules a training event of one or more sessions
    Requires Access Token, Organizer Key and the event details'''
    gtt_url = baseurl+'organizers/'+gtt_organizer_key+'/trainings'
    payload = json.dumps(gtt_event_details)
    gtt_auth = "OAuth oauth_token="+gtt_access_token
    gtt_headers = {'Content-type':'application/json','Accept':'application/json','authorization':gtt_auth}
    r = requests.post(gtt_url,payload,headers=gtt_headers)
    return r.json()
def gttGetTrainingEvents(gtt_access_token,gtt_organizer_key):
    '''Retrieves information on all future scheduled training events for a given organizer
    Requires Access Token and Organizer Key'''
    gtt_url = baseurl+'organizers/'+gtt_organizer_key+'/trainings'
    gtt_auth = "OAuth oauth_token="+gtt_access_token
    gtt_headers = {'Content-type':'application/json','Accept':'application/json','authorization':gtt_auth}
    r = requests.get(gtt_url,headers=gtt_headers)
    return r.json()	
def gttGetTrainingEvent(gtt_access_token,gtt_organizer_key,gtt_training_key):
    '''Uses the organizer key and training key to retrieve information on a future or past training event
    Requires Access Token, Organizer Key and a Training Key'''
    gtt_url = baseurl+'organizers/'+gtt_organizer_key+'/trainings/'+gtt_training_key
    gtt_auth = "OAuth oauth_token="+gtt_access_token
    gtt_headers = {'Content-type':'application/json','Accept':'application/json','authorization':gtt_auth}
    r = requests.get(gtt_url,headers=gtt_headers)
    return r.json()
def gttDeleteTrainingEvent(gtt_access_token,gtt_organizer_key,gtt_training_key):
    '''Deletes a scheduled or completed training. For scheduled trainings, it deletes all scheduled sessions of the training. For completed trainings, the sessions remain in the database
    Requires Access Token, Organizer Key and Training Key'''
    gtt_url = baseurl+'organizers/'+gtt_organizer_key+'/trainings/'+gtt_training_key
    gtt_auth = "OAuth oauth_token="+gtt_access_token
    gtt_headers = {'Content-type':'application/json','Accept':'application/json','authorization':gtt_auth}
    r = requests.delete(gtt_url,headers=gtt_headers)
    return r
def gttGetManagementURLForTrainingEvent(gtt_access_token,gtt_organizer_key,gtt_training_key):
    '''request for a direct URL to the admin portal for a specific training
    Requires Access Token, Organizer Key and Training Key'''
    gtt_url = baseurl+'organizers/'+gtt_organizer_key+'/trainings/'+gtt_training_key+'/manageUrl'
    gtt_auth = "OAuth oauth_token="+gtt_access_token
    gtt_headers = {'Content-type':'application/json','Accept':'application/json','authorization':gtt_auth}
    r = requests.get(gtt_url,headers=gtt_headers)
    return r.json()
def gttUpdateTrainingEventDetails(gtt_access_token,gtt_organizer_key,gtt_event_details):
    '''Update a scheduled training name and description
    Requires Access Token, Organizer Key, Training Key and a JSON object with new name and description'''
    gtt_url = baseurl+'organizers/'+gtt_organizer_key+'/trainings/'+gtt_training_key+'/nameDescription'
    gtt_auth = "OAuth oauth_token="+gtt_access_token
    gtt_headers = {'Content-type':'application/json','Accept':'application/json','authorization':gtt_auth}
    payload = json.dumps(gtt_event_details)
    r = requests.put(gtt_url,payload,headers=gtt_headers)
    return r
def gttGetTrainingEventOrganizers(gtt_access_token,gtt_organizer_key,gtt_training_key):
    '''Retrieves organizer details for a specific training
    Requires Access Token, Organizer Key, and Training Key'''
    gtt_url = baseurl+'organizers/'+gtt_organizer_key+'/trainings/'+gtt_training_key+'/organizers'
    gtt_auth = "OAuth oauth_token="+gtt_access_token
    gtt_headers = {'Content-type':'application/json','Accept':'application/json','authorization':gtt_auth}
    r = requests.get(gtt_url,headers=gtt_headers)
    return r.json()
def gttUpdateTrainingEventOrganizers(gtt_access_token,gtt_organizer_key,gtt_training_key,gtt_event_details):
    '''Replaces the co-organizers for a specific future training event. The scheduling organizer cannot be unassigned.
    Requires Access Token, Organizer Key, Training Key, body (json details of organizers)'''
    gtt_url = baseurl+'organizers/'+gtt_organizer_key+'/trainings/'+gtt_training_key+'/organizers'
    gtt_auth = "OAuth oauth_token="+gtt_access_token
    gtt_headers = {'Content-type':'application/json','Accept':'application/json','authorization':gtt_auth}
    payload = json.dumps(gtt_event_details)
    r = requests.put(gtt_url,payload,headers=gtt_headers)
    return r
def gttUpdateTrainingEventRegistrationSettings(gtt_access_token,gtt_organizer_key,gtt_training_key,gtt_event_details):
    '''Enable or disable web registrations and confirmation emails to registrants
    Requires Access Token, Organizer Key, Training Key, body (json details)'''
    gtt_url = baseurl+'organizers/'+gtt_organizer_key+'/trainings/'+gtt_training_key+'/registrationSettings'
    gtt_auth = "OAuth oauth_token="+gtt_access_token
    gtt_headers = {'Content-type':'application/json','Accept':'application/json','authorization':gtt_auth}
    payload = json.dumps(gtt_event_details)
    r = requests.put(gtt_url,payload,headers=gtt_headers)
    return r
def gttGetStartURLForTrainingEvent(gtt_access_token,gtt_organizer_key,gtt_training_key):
    '''Returns a URL that can be used to start a training. When this URL is opened in a web browser, the GoToTraining client will be downloaded and launched and the training will start after the organizer logs in
    Requires Access Token, Organizer Key and Training Key'''
    gtt_auth = "OAuth oauth_token="+gtt_access_token
    gtt_headers = {'Content-type':'application/json','Accept':'application/json','authorization':gtt_auth}
    gtt_url = baseurl+'organizers/'+gtt_organizer_key+'/trainings/'+gtt_training_key+'/startUrl'
    r = requests.get(gtt_url,headers=gtt_headers)
    return r	
def gttStartTrainingEvent(gtt_access_token,gtt_organizer_key,gtt_training_key) :
    '''Returns a URL that can be used to start a training. When this URL is opened in a web browser, the GoToTraining client will be downloaded and launched and the training will start
    Requires Access Token, Organizer Key and Training Key'''
    gtt_auth = "OAuth oauth_token="+gtt_access_token
    gtt_headers = {'Content-type':'application/json','Accept':'application/json','authorization':gtt_auth}
    gtt_url = baseurl+'trainings/'+gtt_training_key+'/start'
    r = requests.get(gtt_url,headers=gtt_headers)
    return r.json()
def gttUpdateTrainingTimes(gtt_access_token,gtt_organizer_key,gtt_training_key,gtt_event_details):
    '''update a scheduled training's start and end times. If the request contains "notifyTrainers = true" and "notifyRegistrants = true", both organizers and registrants are notified. The response provides the number of notified trainers and registrants
    Requires Access Token, Organizer Key, Training Key and JSON object with new details'''
    gtt_auth = "OAuth oauth_token="+gtt_access_token
    gtt_headers = {'Content-type':'application/json','Accept':'application/json','authorization':gtt_auth}
    gtt_url = baseurl+'organizers/'+gtt_organizer_key+'/trainings/'+gtt_training_key+'/times'
    payload = json.dumps(gtt_event_details)
    r = requests.put(gtt_url,payload,headers=gtt_headers)
    return r.json()
def gttGetRecordingsForTrainingEvent(gtt_access_token,gtt_organizer_key,gtt_training_key):
    '''retrieves information on all online recordings for a given training. If there are none, it returns an empty list
    Requires Access Token and Training Key'''
    gtt_auth = "OAuth oauth_token="+gtt_access_token
    gtt_headers = {'Content-type':'application/json','Accept':'application/json','authorization':gtt_auth}
    gtt_url = baseurl+'trainings/'+gtt_training_key+'/recordings'
    r = requests.get(gtt_url,headers=gtt_headers)
    return r.json()
def gttGetDownloadURLForRecording(gtt_access_token,gtt_training_key,gtt_recording_id):
    '''provides the download for the given recording by returning a 302 redirect to the original file
    Requires Access Token, Training Key and a Recording ID'''
    gtt_auth = "OAuth oauth_token="+gtt_access_token
    gtt_headers = {'Content-type':'application/json','Accept':'application/json','authorization':gtt_auth}
    gtt_url = baseurl+'trainings/'+gtt_training_key+'/recordings/'+gtt_recording_id
    r = requests.get(gtt_url,headers=gtt_headers)
    return r.json()
def gttRegisterStudentOnTrainingEvent(gtt_access_token,gtt_organizer_key,gtt_training_key,gtt_student_details):
    '''Registers one person, identified by a unique email address, for a training. Approval is automatic unless payment or approval is required. The response contains the Confirmation page URL and Join URL for the registrant
    Requires Access Token, Organizer Key, Training Key and JSON object with the student details'''
    gtt_auth = "OAuth oauth_token="+gtt_access_token
    gtt_headers = {'Content-type':'application/json','Accept':'application/json','authorization':gtt_auth}
    gtt_url = baseurl+'organizers/'+gtt_organizer_key+'/trainings/'+gtt_training_key+'/registrants'
    payload = json.dumps(gtt_student_details)
    r = requests.post(gtt_url,payload,headers=gtt_headers)
    return r.json()
def gttGetTrainingEventRegistrants(gtt_access_token,gtt_organizer_key,gtt_training_key):
    '''Retrieves details on all registrants for a past or future training event. Registrants can be:
    WAITING - registrant registered and is awaiting approval (where organizer has required approval)
    APPROVED - registrant registered and is approved
    DENIED - registrant registered and was not approved.
    You may receive results that are cached for up to 2 hours
    Requires Access Token, Organizer Key, and Training Key'''
    gtt_auth = "OAuth oauth_token="+gtt_access_token
    gtt_headers = {'Content-type':'application/json','Accept':'application/json','authorization':gtt_auth}
    gtt_url = baseurl+'organizers/'+gtt_organizer_key+'/trainings/'+gtt_training_key+'/registrants'
    r = requests.get(gtt_url,headers=gtt_headers)
    return r.json()
def gttGetTrainingEventRegistrant(gtt_access_token,gtt_organizer_key,gtt_training_key,gtt_registrant_key):
    '''Retrieves details on a single registrant for a past or future training event. Registrants can be:
    WAITING - registrant registered and is awaiting approval (where organizer has required approval)
    APPROVED - registrant registered and is approved
    DENIED - registrant registered and was not approved.
    You may receive results that are cached for up to 2 hours
    Requires Access Token, Organizer Key, Training Key and Registrant Key'''
    gtt_auth = "OAuth oauth_token="+gtt_access_token
    gtt_headers = {'Content-type':'application/json','Accept':'application/json','authorization':gtt_auth}
    gtt_url = baseurl+'organizers/'+gtt_organizer_key+'/trainings/'+gtt_training_key+'/registrants/'+gtt_registrant_key
    r = requests.get(gtt_url,headers=gtt_headers)
    return r.json()
def gttCancelRegistration(gtt_access_token,gtt_organizer_key,gtt_training_key,gtt_registrant_key):
    '''cancels a registration in a scheduled training for a specific registrant
    Requires Access Token, Organizer Key, Training Key, Registrant Key'''
    gtt_auth = "OAuth oauth_token="+gtt_access_token
    gtt_headers = {'Content-type':'application/json','Accept':'application/json','authorization':gtt_auth}
    gtt_url = baseurl+'organizers/'+gtt_organizer_key+'/trainings/'+gtt_training_key+'/registrants/'+gtt_registrant_key
    r = requests.delete(gtt_url,headers=gtt_headers)
    return r
def gttGetSessionsByDate(gtt_access_token,gtt_organizer_key,gtt_date_details):
    '''Returns all session details over a given date range for a given organizer. A session is a completed training event
    Requires Access Token, Organizer Key, Dates as a JSON object'''
    gtt_auth = "OAuth oauth_token="+gtt_access_token
    gtt_headers = {'Content-type':'application/json','Accept':'application/json','authorization':gtt_auth}
    gtt_url = baseurl+'reports/organizers/'+gtt_organizer_key+'/sessions'
    payload = json.dumps(gtt_date_details)
    r = requests.post(gtt_url,payload,headers=gtt_headers)
    return r.json()
def gttGetAttendanceBySession(gtt_access_token,gtt_organizer_key,gtt_session_key):
    gtt_auth = "OAuth oauth_token="+gtt_access_token
    gtt_headers = {'Content-type':'application/json','Accept':'application/json','authorization':gtt_auth}
    gtt_url = baseurl+'reports/organizers/'+gtt_organizer_key+'/sessions/'+gtt_session_key+'/attendees'
    r = requests.get(gtt_url,headers=gtt_headers)
    return r.json()
def gttGetSessionsByTrainingKey(gtt_access_token,gtt_organizer_key,gtt_training_key):
    '''returns session details for a given training. A session is a completed training event. Each training may contain one or more sessions
    Requires Access Token, Organizer Key, Training Key'''
    gtt_auth = "OAuth oauth_token="+gtt_access_token
    gtt_headers = {'Content-type':'application/json','Accept':'application/json','authorization':gtt_auth}
    gtt_url = baseurl+'reports/organizers/'+gtt_organizer_key+'/trainings/'+gtt_training_key
    r = requests.get(gtt_url,headers=gtt_headers)
    return r.json()

'''organizers = gttGetOrganizers(gtt_access_token,gtt_account_key)
for organizer in organizers:
    print "Details for organizer:",organizer['email']
    for key,value in organizer.iteritems():
        print "\t%-20s: %-30s" % (key,value)
'''
#get all future training events
'''
events = gttGetTrainingEvents(gtt_access_token,gtt_organizer_key)
for event in events:
    for key,value in event.iteritems():
        print "\t%-20s: %-30s" % (key,value)
    print "------------------------"
'''
#Get Sessions by Date Range
gtt_date_details = {
  "startDate": "2017-01-01T00:00:00Z",
  "endDate": "2019-01-01T00:00:00Z"
}
sessions = gttGetSessionsByDate(gtt_access_token,gtt_organizer_key,gtt_date_details)
for session in sessions:
    if session['attendanceCount'] == 0:
        continue
    oldtrainingName = session['trainingName']
    newtrainingName = oldtrainingName.replace(":", " -")
    attendance = gttGetAttendanceBySession(gtt_access_token,gtt_organizer_key,session['sessionKey'])
    for attend in attendance:
        if attend['timeInSession'] == 0:
            continue
        print session['sessionStartTime'][:10]+","+newtrainingName+","+attend['givenName'],attend['surname']+","+attend['email']
