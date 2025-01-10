import pytest
from app.app import app


def test_upload_image():
    with app.test_client() as client:
        data = {
            'file': (io.BytesIO(b"test image data"), "test_image.jpg")
        }
        response = client.post('/images', data=data, content_type='multipart/form-data')
        assert response.status_code == 200
        assert response.json['message'] == "Image uploaded successfully!"


def test_get_images():
    with app.test_client() as client:
        response = client.get('/images')
        assert response.status_code == 200
        assert isinstance(response.json, list)
