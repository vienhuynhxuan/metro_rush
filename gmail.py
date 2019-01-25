from __future__ import print_function
from googleapiclient.discovery import build
# from apiclient import errors
import googleapiclient
from httplib2 import Http
from email.mime.text import MIMEText
import base64
from google.oauth2 import service_account
from authentication import authenticated

# Email variables. Modify this!
EMAIL_FROM = 'vienhuynhxuan@gmail.com'
EMAIL_TO = 'titeo.messi@gmail.com'
EMAIL_SUBJECT = 'Hello  from Lyfepedia!'
EMAIL_CONTENT = 'Hello, this is a test email.'


def create_message(sender, to, subject, message_text):
  """Create a message for an email.
  Args:
    sender: Email address of the sender.
    to: Email address of the receiver.
    subject: The subject of the email message.
    message_text: The text of the email message.
  Returns:
    An object containing a base64url encoded email object.
  """
  message = MIMEText(message_text)
  message['to'] = to
  message['from'] = sender
  message['subject'] = subject
  string = base64.urlsafe_b64encode(message.as_bytes())
  string = string.decode()
  return {'raw': string}


def send_message(service, user_id, message):
  """Send an email message.

  Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    message: Message to be sent.

  Returns:
    Sent Message.
  """
  # message = (service.users().messages().send(userId=user_id, body=message))
  # print(message)
  # # print("------------")
  # message.execute()
  try:
    message = (service.users().messages().send(userId=user_id, body=message)
               .execute())
    print ('Message Id: %s' % message['id'])
    return message
  except googleapiclient.errors.HttpError as error:
    print ('An error occurred: %s' % error)



service = authenticated()
# Call the Gmail API
message = create_message(EMAIL_FROM, EMAIL_TO, EMAIL_SUBJECT, EMAIL_CONTENT)
sent = send_message(service,'me', message)
