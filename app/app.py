from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import boto3
import os

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = os.getenv("SECRET_KEY")

db = SQLAlchemy(app)

s3_client = boto3.client(
    "s3",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY"),
    aws_secret_access_key=os.getenv("AWS_SECRET_KEY"),
)

S3_BUCKET = os.getenv("AWS_S3_BUCKET")


class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(120), nullable=False)
    s3_url = db.Column(db.String(255), nullable=False)


@app.route('/')
def home():
    return "Hello, this is the Image Publisher app!"


@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    s3_client.upload_fileobj(file, S3_BUCKET, file.filename)
    s3_url = f"https://{S3_BUCKET}.s3.amazonaws.com/{file.filename}"

    new_file = File(filename=file.filename, s3_url=s3_url)
    db.session.add(new_file)
    db.session.commit()

    return jsonify({"message": "File uploaded successfully", "s3_url": s3_url})


@app.route('/images', methods=['GET'])
def get_images():
    return jsonify({"images": "images"}), 200


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5555)
