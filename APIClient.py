import cognitive_face as CF
from APIKey import *
import glob
import firebase_admin
from firebase_admin import credentials, db
from hashlib import md5

cred = credentials.Certificate('project-anti-alz-firebase-adminsdk-zlh54-decaa0ce0a.json') 
firebase_admin.initialize_app(cred, {'databaseURL' : 'https://project-anti-alz.firebaseio.com/'})
#default_app = firebase_admin.initialize_app(cred)
root = db.reference()

# Imports the Google Cloud client library
from google.cloud import storage

# Instantiates a client
storage_client = storage.Client()

# The name for the new bucket
bucket_name = 'training-images-3519435695'

# Creates the new bucket
# bucket = storage_client.create_bucket(bucket_name)

# print('Bucket {} created.'.format(bucket.name))
"""
2019 Cruzhacks
"""
class APIClient:

    def __init__(self, db_id):
        self.BASE_URL = 'https://westus.api.cognitive.microsoft.com/face/v1.0/'
        self.PERSON_GROUP_ID = db_id
        CF.BaseUrl.set(self.BASE_URL)
        CF.Key.set(SUB_KEY)

    def create_database(self, name):
        CF.person_group.create(self.PERSON_GROUP_ID, name)

    def add_person(self, name, user_data, img_dir):
        response = CF.person.create(self.PERSON_GROUP_ID, name, user_data)
        person_id = response["personId"] 
        ref = CF.person.get(self.PERSON_GROUP_ID, person_id)
        user_ref = root.child('users')
        user_ref.child(person_id).set(
            {
                "name" : ref['name'], 
                "userData" : ref['userData'], 
                "imgUrls": [], 
                "msg" : "You met " + ref["name"] + " he is your " + ref["userData"] + ".",
                "additionalMsg" : "Replace Me"
            }
        )

        for img in glob.glob(img_dir):
            CF.person.add_face(img, self.PERSON_GROUP_ID, person_id)
            # now we need to add imgs to cloud in here
            """Uploads a file to the bucket."""
            storage_client = storage.Client()
            bucket = storage_client.get_bucket(bucket_name)
            destination_blob_name = md5(img.encode('utf-8')).hexdigest()
            blob = bucket.blob(destination_blob_name)
            blob.upload_from_filename(img)

            url = "https://storage.cloud.google.com/training-images-3519435695/"+ destination_blob_name
            root.child('users').child(person_id).child('imgUrls').push(url)

            # new_array = []
            # for img in user_ref["imgUrls"]:
            #     new_array.append(img)
            # new_array.append(url)
            # user_ref.update({'imgUrls':new_array})

            print('File {} uploaded to {}.'.format(img, destination_blob_name))

    def return_message_from_face(self, path_to_img):
        response = CF.face.detect(path_to_img)
        face_ids = [d['faceId'] for d in response]
        identified_faces = CF.face.identify(face_ids, self.PERSON_GROUP_ID)
        person_id = identified_faces[0]['candidates'][0]['personId']
        response = CF.person.get(self.PERSON_GROUP_ID, person_id)
        return response 

    def print_status(self):
        response = CF.person_group.get_status(self.PERSON_GROUP_ID)
        status = response['status']
        print(status)   

    def print_list(self):
        print(CF.person.lists(self.PERSON_GROUP_ID))

    def train_data(self):
        CF.person_group.train(self.PERSON_GROUP_ID)


