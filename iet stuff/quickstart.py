from __future__ import print_function
import pickle
import serial
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pyttsx3
from time import sleep


# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1u6pUPDFWZbnUDTIy4L-cwDK7-RHA9-_ze_j3tgoMf14'
SAMPLE_RANGE_NAME = 'A2:D'

def main():
    engine = pyttsx3.init()
    words = serial.Serial('com4',9600)
    # sleep(0.3)
    # names = serial.Serial('com4', 9600)
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
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

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
    


    #################################################################################
    new_student_id = 0
    values = result.get('values', [])
    length = len(values) - 1 
    counter = length
    while True:
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
    

        values = result.get('values', [])
        length = len(values) - 1  
        name = values[length][1]
        student_id = values[length][2]
        sleep(1)
        if student_id != new_student_id:
            counter +=1
            engine.say("Welcome to the club " + values[length][1])
            engine.runAndWait()
            new_student_id = student_id
            print("Numer of students who joined : " + str(counter) )
            words.write((str(counter) + '\n').encode('UTF-8'))
            sleep(0.3)
            words.write((str(values[length][1]) + '\n').encode('UTF-8'))
            sleep(1)

 






    # if not values:
    #     print('No data found.')
    # else:
    #     print('Name, Major:')
    #     for row in values:
    #         # Print columns A and E, which correspond to indices 0 and 4.
    #         print('%s' % ( row[1]))



if __name__ == '__main__':
    while True:
        main()