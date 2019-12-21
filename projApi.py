from __future__ import print_function
import requests
from google.auth.transport.requests import Request # requests for the mail 
from google_auth_oauthlib.flow import InstalledAppFlow # mail authorisation
from googleapiclient.discovery import build # for interacting with API
from apiclient import errors # apiclient for gmail
import os.path  # to see if files exist or not
import pickle  # gmail uses to store credentials
import json # for using JSON
import dbconfig # the configuration

def getForecast(forecast):
    # Epoch times for this Christmas and last one
    christmas2019 = 1577232000
    christmas2018 = 1545696000
#    url = "https://api.darksky.net/forecast/2630d78877b5d732a00f86409bbab634/90,135"

    # Get the correct URL for each Christmas
    if forecast == "past":
        url = dbconfig.pastURL
    elif forecast == "future":
        url = dbconfig.futureURL
    else:
        # Current URL
        url = dbconfig.currentURL

    # Get weather
    response = requests.get(url)
    data = response.json()
    weather = {}

    # Function to convert the return values to dictionary items
    weather["summary"] = data['currently']['summary']
    weather["icon"] = data['currently']['icon']
    weather["temperature"] = data['currently']['temperature']
    return weather

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def getMail():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds, cache_discovery =False)

    try:
        # Call the Gmail API
        response = service.users().messages().list(userId='me').execute()
        messages = []
        if 'messages' in response:
            messages.extend(response['messages'])
        while 'nextPageToken' in response:
            page_token = response['nextPageToken']
            # Only get unread emails
            response = service.users().messages().list(
                userId='me', q='is: unread', pageToken=page_token).execute()
            messages.extend(response['messages'])
        allMessages = []
        # Loop through each message
        for message in messages:
            msgDict = {}
            completeMessage = service.users().messages().get(
                userId='me', id=message['id']).execute()
            headers = completeMessage['payload']['headers']
            # Get the From, subject and meaasge snippet from each
            msgDict["msgFrom"] = list(filter(lambda h: h['name'] == 'From', headers))[
                0]['value']
            msgDict["msgSubject"] = list(filter(lambda h: h['name'] == 'Subject', headers))[
                0]['value']
            msgDict["msgSnippet"] = completeMessage['snippet']
            # Put them together in a dictionary
            allMessages.append(msgDict)
        # Return all messages
        return allMessages
    # If there are errors...
    except errors.HttpError:
        print ('An error occurred: %s' % errors.HttpError)

# Just used for troubleshooting.
# Putting this in here in case I forget to delete it. 
#if __name__ == '__main__':
#    forecastList = ["current", "future", "past"]
#    weatherResults = []
#    for forecast in forecastList:
#        result = getForecast(forecast)
#        print(result)
#        weatherResults.append(result)
#    print(json.dumps(weatherResults))
