# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['ACb2fad9334a8b6e615c3103ae6fbdac00']
auth_token = os.environ['985cdf4fbf9e2208a955d3ced3078c44']
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+15705144903',
                     to='+15558675310'
                 )

print(message.sid)
