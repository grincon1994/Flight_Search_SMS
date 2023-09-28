from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")
twilio_number = os.getenv("TWILIO_NUMBER")
authorized_twilio_number = os.getenv("AUTH_NUMBER")



class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    
    def __init__(self):
        self.client = Client(account_sid, auth_token)


    def get_notification(self, message):

        message = message = self.client.messages \
                    .create(
                        body=message,
                        from_=twilio_number,
                        to=authorized_twilio_number
                    )
        print(message.sid)
