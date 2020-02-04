def test_home(client):
    response = client.get('/')
    assert 200 == response.status_code

def test_test_page(client):
    response = client.get('/pages?slug=test')
    assert 200 == response.status_code

def test_pages_without_page(client):
    response = client.get('/pages')
    assert 400 == response.status_code

def test_pages_invalid_page(client):
    response = client.get('/pages?slug=nuke_me')
    assert 404 == response.status_code

def test_not_found(client):
    response = client.get('/boobytrap')
    assert 404 == response.status_code

def test_contact_send(client):
    response = client.post('/contact_send', data = dict(email="bla", subject="hu", text="tz"))
    assert 200 == response.status_code