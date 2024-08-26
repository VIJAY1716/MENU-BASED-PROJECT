from twilio.rest import Client

# Your Account SID and Auth Token from twilio.com/console
account_sid = 'AC8bfbe301e6030bce0956626bd854c4ec'
auth_token = '28f003329af144ba5728c12cabe7382c'
client = Client(account_sid, auth_token)

# Message details
from_phone = '+17079435649'
to_phone = '+918608830341'
message_body = 'Hello from Python!'

# Send message
message = client.messages.create(
    body=message_body,
    from_=from_phone,
    to=to_phone
)

print(f'Message sent: {message.sid}')