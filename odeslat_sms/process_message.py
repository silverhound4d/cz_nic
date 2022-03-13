import os
import re

from twilio.rest import Client


INVALID_MESSAGE = 1
INVALID_PHONE_NUMBER = 2

TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_NUM = os.environ.get("TWILIO_NUM")

def validate_number(phone_number: str) -> bool:
    """Validate all accepted phone numbers formats."""
    poss_patterns = ["^\+\d{3}\.\d{9}$", "^\(\d{3}\)\d{3}\-\d{3}\-\d{3}$"]
    for pattern in poss_patterns:
        match = re.search(pattern, phone_number)
        if match:
            return True
    return False

def format_phone_number(phone_number: str) -> str:
    """Convert all accepted/verified phone number formats into one that can actually be used to send messages"""
    formatted_num = re.sub("[+.()-]", "", phone_number)
    formatted_num = f"+{formatted_num}"
    return formatted_num

def validate_message(message: str) -> bool:
    """Validate the message is not empty & does not go over the 255 char limit."""
    if len(message) == 0:
        return False
    elif len(message) > 255:
        return False
    elif len(message) <= 255:
        return True

def send_sms(phone_number: str, message: str, send: bool) -> int:
    """Send SMS using the Twilio client."""
    if send:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        sms = client.messages \
                    .create(
                        body=message,
                        from_=TWILIO_NUM,
                        to=format_phone_number(phone_number)
                    )
        return 0
    print('Message was processed successfully but NOT SENT - Twilio DISABLED')
    return 0

def process_message(phone_number: str, message: str, send: bool) -> int:
    """Main fuction - send out an sms message that pass the validation."""
    if not validate_number(phone_number):
        print("Telefonní číslo může být uvedeno pouze v následujích formátech: +xxx.yyyyyyyyy nebo (xxx)yyy-yyy-yyy.")
        return INVALID_PHONE_NUMBER
    if not validate_message(message):
        print(f"Zpráva musí mít délku mezi 1-255 znaků. Vaše zpráva obsahuje {len(message)} znaků!")
        return INVALID_MESSAGE
    return send_sms(phone_number, message, send)

