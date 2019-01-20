from flask import Flask, render_template, jsonify, request
from flask_bootstrap import Bootstrap
import base64
from hashlib import md5
from APIClient import *

# Imports the Google Cloud client library
from google.cloud import storage

# Instantiates a client
storage_client = storage.Client()

# The name for the new bucket
bucket_name = 'training-images-3519435695'
"""

"""
app = Flask(__name__)
bootstrap = Bootstrap(app)
client = APIClient("people_three")

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/detect-face', methods=['POST'])
def detect_face():
    img_content = request.data
    decoded_img = base64.b64decode(img_content)
    img_path = "uploads/" + md5(img_content.decode().encode('utf-8')).hexdigest() + ".png"
    with open(img_path, "wb") as fh:
        fh.write(decoded_img)

    """Uploads a file to the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    destination_blob_name = md5(img_content.decode().encode('utf-8')).hexdigest()
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename("uploads/" + destination_blob_name + ".png")
    print('File {} uploaded to {}.'.format("uploads/" + destination_blob_name + ".png", destination_blob_name))

    url = "https://storage.cloud.google.com/training-images-3519435695/"+ destination_blob_name

    # result = client.return_message_from_face(img_path)
    # result['msg'] = "You met " + result["name"] + " he is your " + result["userData"] + "."
    # return jsonify(result)

@app.route('/reminders', methods=['GET'])
def get_reminders():
    pass

if __name__=='__main__':
    app.run(debug=True)
