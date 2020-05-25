from django.core.mail import send_mail
from django.utils.crypto import get_random_string


def send_verification(code, email):
    status = False
    subject = 'Email Verification'
    body = f'Your verification code is {code}'
    sender = 'noreply@unofficialncit.com'
    receiver = email

    try:
        send_mail(subject, body, sender, [receiver], fail_silently = False)
        status = True

    except Exception as e:
        print(e)

    return status


def generate_token():
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&amp;*(-_=+)'
    token = get_random_string(50, chars)
    return token