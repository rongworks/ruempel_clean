import pytest

from app.models.contact_request import ContactRequest

from_email = "ladida@abc.de"
from_subject = "Test Subject"
from_text = "ABC DEF GHI"

def test_init_blank():
    contact = ContactRequest()

    assert contact.email is None
    assert contact.subject == 'Request'
    assert contact.text == ''

def test_init():

    contact = ContactRequest(from_email, from_subject, from_text)

    assert contact.email == from_email
    assert contact.subject == from_subject
    assert contact.text == from_text

def test_set_from_params():
    params = {'email': from_email,
              'subject': from_subject,
              'text': from_text}

    contact = ContactRequest().from_params(params)
    assert contact.email == from_email
    assert contact.subject == from_subject
    assert contact.text == from_text

def test_is_valid():
    invalid_contact = ContactRequest()
    valid_contact = ContactRequest(from_email, from_subject, from_text)
    assert invalid_contact.is_valid() == False
    assert valid_contact.is_valid() == True

def test_send_invalid_request():
    invalid_contact = ContactRequest()
    assert invalid_contact.send() == False

def test_send_request():
    contact = ContactRequest(from_email, from_subject, from_text)
    assert contact.send() == True