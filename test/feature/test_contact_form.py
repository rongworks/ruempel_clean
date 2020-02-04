import re

from splinter import Browser

from app.config.router import Router
def test_contact(flask_app):

    browser = Browser('flask', app=flask_app)

    goto_contact_page(browser)

    send_request(browser)

    browser.quit()

def goto_contact_page(browser):
    expected_text = 'Email Adresse'

    contact_page = '/pages?slug=contact'

    browser.visit(contact_page)
    assert browser.find_by_css('form'), "Could not find <form> element"
    assert browser.find_by_text(expected_text), f'Did not find: {expected_text} in {browser.url}  {browser.html}'

def send_request(browser):
    confirm_page = '/pages?slug=contact_confirm'
    #TODO: Seems validation is ignored here..
    browser.find_by_name('send').first.click()

    assert confirm_page == browser.url, f"Current URL {browser.url} did not match page contact_confirm"