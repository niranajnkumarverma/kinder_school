from twilio.rest import Client
import os

account_sid = 'AC60080740b62ffb0f41ba034a3c113c68'
auth_token = '0bd91b5fd10f3dd2430d61a2a38f21b6'
client = Client(account_sid, auth_token)


def send_sms(user_code, mobile):
    message = client.messages.create(
        body=f'Hii! kinder School Verification code is {user_code}',
        from_='	+17015578690',
        # to=f'{mobile}'
        to='+918340738572'
    )

    print(message.sid)


