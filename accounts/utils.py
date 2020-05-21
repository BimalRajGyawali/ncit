from django.core.mail import send_mail


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
