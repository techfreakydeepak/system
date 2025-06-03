from flask import current_app
import random
import string

def generate_otp(length=6):
    """Generate a random OTP of specified length."""
    otp = ''.join(random.choices(string.digits, k=length))
    return otp

def send_otp(mobile_number, otp):
    """Send the generated OTP to the user's mobile number."""
    # Here you would integrate with an SMS service to send the OTP
    # For example, using the functions in src/utils/sms.py
    current_app.logger.info(f"Sending OTP {otp} to {mobile_number}")
    # sms.send_sms(mobile_number, f"Your OTP is: {otp}")

def verify_otp(input_otp, generated_otp):
    """Verify the input OTP against the generated OTP."""
    return input_otp == generated_otp