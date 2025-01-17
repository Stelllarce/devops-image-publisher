from flask import Flask, jsonify, request


app = Flask(__name__)


# In-memory storage for images (just a mock)
images = []


@app.route('/')
def home():
    return "Hello, this is the Image Publisher app!"


@app.route('/images', methods=['POST'])
def upload_image():
    image = request.json.get('image')
    if not image:
        return jsonify({"error": "No image provided"}), 400
    images.append(image)
    return jsonify({"message": "Image uploaded successfully!",
                    "images": images}), 201


@app.route('/images', methods=['GET'])
def get_images():
    return jsonify({"images": images}), 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
