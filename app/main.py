from flask import Flask, request, jsonify
from app.database import db_session
from app.models import Image


app = Flask(__name__)


@app.route('/images', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400
    file = request.files['file']
    new_image = Image(name=file.filename, data=file.read())
    db_session.add(new_image)
    db_session.commit()
    return jsonify({"message": "Image uploaded successfully!"}), 200


@app.route('/images', methods=['GET'])
def get_images():
    images = Image.query.all()
    if not images:
        return jsonify([]), 200
    return jsonify([{"id": img.id, "name": img.name} for img in images]), 200


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == '__main__':
    app.run(debug=True)