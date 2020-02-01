from flask_bootstrap import Bootstrap
from splinter import Browser
from flask import Flask
from ruempel_clean import app

from app.config.router import Router
def test_home():
    expected_text = 'RÜMPEL CLEAN'
    browser = Browser('flask', app=app)
    browser.visit('/')

    assert browser.is_text_present(expected_text), f'Did not find: {expected_text} in {browser.url}  {browser.html}'

    browser.quit()