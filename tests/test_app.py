import io
import pytest
from app.app import app, db


@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.session.remove()
            db.drop_all()


def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b"Hello, this is the Image Publisher app!"


def test_upload_image(client):
    data = {
        'file': (io.BytesIO(b"dummy file content"), 'test_image.png')
    }
    response = client.post('/upload', data=data, content_type='multipart/form-data')
    assert response.status_code == 200
    assert response.json['message'] == "File uploaded successfully"
    assert response.json['s3_url'].endswith('test_image.png')


def test_get_images(client):
    response = client.get('/images')
    assert response.status_code == 200
    assert "images" in response.json['images']
