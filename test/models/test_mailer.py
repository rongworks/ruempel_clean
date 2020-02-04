import pytest

from flask_mail import _Mail
from app.models.mailer import Mailer
from app.models.contact_request import ContactRequest

def test_init():
    mailer = Mailer()

def test_send_contact_request():
    # We need context here, is covered by feature tests
    pass
