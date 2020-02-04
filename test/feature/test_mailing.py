import pytest
from flask_mail import Mail

from app.models.contact_request import ContactRequest
from app.models.mailer import Mailer


def test_mail(flask_app):
    mailer = Mailer()
    mail = Mail(flask_app)
    #fl.testing = True
    with flask_app.test_request_context('/'):
        with mail.record_messages() as outbox:
            mailer.send_contact_request(ContactRequest("test@example.com","test","test")).send(mail)
            assert len(outbox) == 1
            assert outbox[0].subject == "[Contact] test"