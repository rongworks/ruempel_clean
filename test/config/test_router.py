def test_home(client):
    response = client.get('/')
    assert response.status_code == 200

def test_test_page(client):
    response = client.get('/pages?slug=test')
    assert response.status_code == 200

def test_not_found(client):
    response = client.get('/boobytrap')
    assert response.status_code == 404