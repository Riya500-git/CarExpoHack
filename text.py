import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
def textme():

    account_sid = 'AC1aa61ef4d890feb1931e8f26c3f7e7b6'
    auth_token = 'eb1cfa1e3a5a693c932b75579a4c219c'
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            body='Your car is getting towed!',
            from_='+19032731446',
            to='+16194058727'
        )
    print(message.sid)