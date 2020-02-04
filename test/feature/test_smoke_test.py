from splinter import Browser

def test_home(flask_app):
    expected_text = 'RÜMPEL CLEAN'
    browser = Browser('flask', app=flask_app)
    browser.visit('/')

    assert browser.is_text_present(expected_text), f'Did not find: {expected_text} in {browser.url}  {browser.html}'

    browser.quit()