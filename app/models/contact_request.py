from app.models.mailer import Mailer

class ContactRequest:

    def __init__(self, email=None, subject='Request', text=''):
        self.email = email
        self.subject = subject
        self.text = text
        self.receiver = "info@rongworks.de"


    def from_params(self, params):
        self.email = params['email']
        self.subject = params['subject']
        self.text = params['text']

        return self

    def is_valid(self):
        if self.email is None:
            return False
        return True