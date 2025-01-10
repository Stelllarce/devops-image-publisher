import pytest
import io
from app.main import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_upload_image(client):
    data = {
        'file': (io.BytesIO(b"test image data"), "test_image.jpg")
    }
    response = client.post('/images', data=data, content_type='multipart/form-data')
    assert response.status_code == 200
    assert response.json is not None
    assert response.json['message'] == "Image uploaded successfully!"


def test_get_images(client):
    response = client.get('/images')
    assert response.status_code == 500
    assert response.json is not None
    assert isinstance(response.json, list)
