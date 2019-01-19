import cognitive_face as CF
from APIKey import *
"""

"""

BASE_URL = 'https://westus.api.cognitive.microsoft.com/face/v1.0/'
PERSON_GROUP_ID = "people_two"
CF.BaseUrl.set(BASE_URL)
CF.Key.set(SUB_KEY)

def return_message_from_face(path_to_img):


    response = CF.face.detect(path_to_img)
    face_ids = [d['faceId'] for d in response]
    #print(face_ids)

    identified_faces = CF.face.identify(face_ids, PERSON_GROUP_ID)
    #print(identified_faces)

    person_id = identified_faces[0]['candidates'][0]['personId']
    response = CF.person.get(PERSON_GROUP_ID, person_id)
    return(response)

#print(return_message_from_face("tejas-test.jpg"))
