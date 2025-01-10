import pytest
from app.app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b"Hello, this is the Image Publisher app!"


def test_upload_image(client):
    response = client.post('/images', json={"image": "image1.png"})
    assert response.status_code == 201
    assert response.json['message'] == "Image uploaded successfully!"
    assert "image1.png" in response.json['images']


def test_get_images(client):
    client.post('/images', json={"image": "image2.png"})
    response = client.get('/images')
    assert response.status_code == 200
    assert "image2.png" in response.json['images']
