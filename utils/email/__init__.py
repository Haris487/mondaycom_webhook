from .sendgrid_wrapper import SendGridWrapper
import os

class Email(object):
  wrapper_class = SendGridWrapper

  def __init__(self):
    from_email = os.environ.get("FROM_EMAIL")
    to = os.environ.get("TO_EMAIL")
    self.wrapper = self.wrapper_class(from_email, to)

  def send(self, subject, content):
    response = self.wrapper.send_email(subject, content)
    return response