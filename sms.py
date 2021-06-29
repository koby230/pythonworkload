

import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = "AC6bc10482c274a646b43322cbf43fbe79"
auth_token = "c7bf3aea01e476fc4a30474174b49763"
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Heyyyy what's good this is a test.",
                     from_='+18582957306',
                     to='+17206098585'
                 )

print(message.sid)