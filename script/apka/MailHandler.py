from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os
from utils import textReader

class MailHandler:
    def __init__(self):
        self.SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
        self.creds = None
        self.service = None
        self.checkCredentails()
        self.messages = None
        self.offset = 0

    def checkCredentails(self):
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', self.SCOPES)
                creds = flow.run_local_server(port=0)

            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        self.service = build('gmail', 'v1', credentials=creds)

    def getMails(self):
        self.messages = self.service.users().messages().list(userId='lamazlo21@gmail.com', labelIds=['INBOX'], q='is:unread').execute()
        messagesCounter = 0
        for message in self.messages['messages']:
            messagesCounter += 1
        text = 'Masz ' + str(messagesCounter) + ' nieodczytanych wiadomości, czy chcesz je usłyszeć?'
        textReader(text)

    def readMails(self):
        messageSender = 'Wiadomość od użytkownika '
        messageSubject = ', Temat wiadomości, '
        count = 0
        for i in range(self. offset, self.offset + 3):
            msg = self.service.users().messages().get(userId='lamazlo21@gmail.com', id=self.messages['messages'][i]['id']).execute()
            data = msg['payload']['headers']
            for values in data:
                if values['name'] == 'Subject':
                    messageSubject += values['value']
                if values['name'] == 'From':
                    sender = values['value'].split('<')[0]
                    messageSender += sender
            text = messageSender + messageSubject
            textReader(text)
            messageSender = 'Wiadomość od użytkownika '
            messageSubject = ', Temat wiadomości, '
            if count == 2:
                text = 'Czy chcesz usłyszeć więcej wiadomości?'
                textReader(text)
                self.offset = self.offset + 3
                break
            count += 1

    def stopReading(self):
            self.offset = 0
            return None