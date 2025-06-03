from twilio.rest import Client

def send_sms(to, message):
    # Your Account SID and Auth Token from twilio.com/console
    account_sid = 'your_account_sid'
    auth_token = 'your_auth_token'
    
    client = Client(account_sid, auth_token)

    # Sending the SMS
    client.messages.create(
        to=to,
        from_='your_twilio_phone_number',
        body=message
    )

def verify_otp(phone_number, otp):
    # Logic to verify the OTP sent to the phone number
    # This is a placeholder for actual verification logic
    return True  # Assume verification is successful for now