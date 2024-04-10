from twilio.rest import Client
from os import environ

SID = environ["TWILIO_SID"]
TOKEN = environ["TWILIO_TOKEN"]

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.

    def sendtext(self, body):
        print(body)

#        client = Client(SID, TOKEN)
#        message = client.messages.create(
#            from_="+16815395838",
#            body=body,
#            to='+36303434808'
#        )
#
#        print(message.sid)

