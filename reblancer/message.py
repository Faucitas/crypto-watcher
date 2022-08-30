import os
from typing import Dict, Optional

import dotenv
from twilio.rest import Client


dotenv.load_dotenv()

TWILIO_ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
TWILIO_AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']
TWILIO_MESSAGE_SID = os.environ['TWILIO_MESSAGE_SID']
TWILIO_SENDING_NUMBER = os.environ['MY_PHONE_NUMBER']


def send_text_message(message):
    # Send a message with the percentage
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        messaging_service_sid=TWILIO_MESSAGE_SID,
        body=message,
        to=TWILIO_SENDING_NUMBER
    )