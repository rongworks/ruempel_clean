def test_home(client):
    response = client.get('/')
    assert response.status_code == 200

def test_test_page(client):
    response = client.get('/pages?slug=test')
    assert response.status_code == 200

def test_pages_without_page(client):
    response = client.get('/pages')
    assert response.status_code == 400

def test_pages_invalid_page(client):
    response = client.get('/pages?slug=nuke_me')
    assert response.status_code == 404

def test_not_found(client):
    response = client.get('/boobytrap')
    assert response.status_code == 404