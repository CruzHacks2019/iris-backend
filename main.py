from flask import Flask, render_template, jsonify, request
from flask_bootstrap import Bootstrap
from flask_cors import CORS
import base64
from hashlib import md5
from APIClient import *
import firebase_admin
from firebase_admin import credentials, db
import time
import json

cred = credentials.Certificate('project-anti-alz-firebase-adminsdk-zlh54-decaa0ce0a.json') 
# firebase_admin.initialize_app(cred, {'databaseURL' : 'https://project-anti-alz.firebaseio.com/'})
root = db.reference()

# Imports the Google Cloud client library
from google.cloud import storage

# The name for the new bucket
bucket_name = 'history-images-3519435695'
# bucket = storage_client.create_bucket(bucket_name)
"""

"""
app = Flask(__name__)
CORS(app)
bootstrap = Bootstrap(app)
client = APIClient("people_13")

epoch = lambda: int(time.time() * 1000)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/detect-face', methods=['POST'])
def detect_face():
    start_time = time.time()

    img_content = request.data
    decoded_img = base64.b64decode(img_content)
    
    start_decode_time = time.time()
    filename = md5(img_content.decode().encode('utf-8')).hexdigest()
    end_decode_time = time.time()
    print("total time to decode: " + str(end_decode_time - start_decode_time))

    img_path = "uploads/" + filename + ".jpg"
    with open(img_path, "wb") as fh:
        fh.write(decoded_img)

    start_upload_time = time.time()

    """Uploads a file to the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    destination_blob_name = filename
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(img_path)
    print('File {} uploaded to {}.'.format(img_path, destination_blob_name))

    end_upload_time = time.time()
    print("total time to upload: " + str(end_upload_time - start_upload_time))

    url = "https://storage.cloud.google.com/history-images-3519435695/"+ destination_blob_name

    start_face_time = time.time()

    result = client.return_message_from_face(img_path)

    end_face_time = time.time()
    print("total time to face identify: " + str(end_face_time - start_face_time))

    end_time = time.time()
    print("total time (1): " + str(end_time - start_time))

    # this is a list now, what happens if the list is empty?
    print(result)
    if len(result) > 0:
        # result[0]['msg'] = "You met " + result[0]["name"] + " he is your " + result[0]["userData"] + "."
        print(result)
    else:
        # print("Empty List")
        return(jsonify({"error": "I'm sorry. I don't see anyone else."}))


    hist_ref = root.child('history')
    for person_id, person_info in result.items():
        hist_ref.child(str(epoch()) + '|' + person_id).set(
            {
                'imgUrls': url,
                'personId': person_id
            }
        )
    
    end_time = time.time()
    print("total time (2): " + str(end_time - start_time))

    return jsonify(result)

@app.route('/reminders', methods=['GET'])
def get_reminders():
    return jsonify(client.fetch_all_reminders())

@app.route("/update_azure_db", methods=['POST'])
def update_azure_db():
    # print(request.json)
    data = request.json
    # json_data = request.data
    # json_file = open('json1')
    # json_str = json_file.read()
    # data = json.loads(json_str)[0]
    base64image = data["file"].split(',')[-1]

    decoded_img = base64.b64decode(base64image)
    img_path = "uploads/" + md5(base64image.encode('utf-8')).hexdigest() + ".jpg"
    with open(img_path, "wb") as fh:
        fh.write(decoded_img)
    client.add_person(data["name"], data["relation"], img_path, data["notes"])
    client.train_data()
    client.print_list()
    print("/update_azure_db called")
    return jsonify({"error": "Do not access"})

@app.route("/get_history", methods=["POST"])
def get_history():
    users = root.child("history").get()
    return jsonify(users)

if __name__=='__main__':
    app.run(debug=True)
