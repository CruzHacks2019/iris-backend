import cognitive_face as CF
from PIL import Image
import glob
"""
2019 Cruz Hacks
"""

#init
SUB_KEY = '36fee94e28fa469fa8df5deec07c8f1c'
BASE_URL = 'https://westus.api.cognitive.microsoft.com/face/v1.0/'
PERSON_GROUP_ID = "known_persons"
CF.BaseUrl.set(BASE_URL)
CF.Key.set(SUB_KEY)
    
# create Person Object
#
# this already ran, so we should be good

def create_database(name):
    CF.person_group.create(PERSON_GROUP_ID, name)

# now add a person
def add_person(name, user_data, img_dir):
    response = CF.person.create(PERSON_GROUP_ID, name, user_data)
    person_id = response["personId"]
    for img, i in enumerate(glob.glob(img_dir)):
        save_id = name + str(i) + ".jpg"
        print(save_id)
        CF.person.add_face(save_id, PERSON_GROUP_ID, person_id)
    
    CF.person_group.train(PERSON_GROUP_ID)


def add_images(directory):
    for sub_dir in directory:
        add_person(str(sub_dir), "Training Photo", sub_dir)


"""
Run:
"""
#create_database("Known Persons")
add_images("static/")
