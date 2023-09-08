import os
import sendgrid
from sendgrid.helpers.mail import Content, Email, Mail

class SendGridWrapper(object):
    def __init__(self, from_email, to_email):
        self.sg = sendgrid.SendGridAPIClient(
            apikey=os.environ.get("SENDGRID_API_KEY")
        )
        self.from_email = Email(from_email)
        self.to_email = Email(to_email)

    def send_email(self, subject, content):
        mail = Mail(self.from_email, subject, self.to_email, content)
        response = self.sg.client.mail.send.post(request_body=mail.get())
        if response.status_code != 202:
            raise Exception("Error sending email. Status code: {}".format(response.status_code))
        return response