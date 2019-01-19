import cognitive_face as CF
from PIL import Image
import glob
"""
2019 Cruz Hacks
#"""


    
# create Person Object
#
# this already ran, so we should be good

def create_database(name, id):
    CF.person_group.create(id, name)

# now add a person
def add_person(name, user_data, img_dir, id):
    response = CF.person.create(id, name, user_data)
    person_id = response["personId"]
    for img, i in enumerate(glob.glob(img_dir)):
        save_id = name + str(i) + ".jpg"
        print(save_id)
        CF.person.add_face(save_id, id, person_id)
    
    CF.person_group.train(id)
    print(CF.person_group.get_status(id))

def add_images(directory, id):
    for sub_dir in directory:
        add_person(str(sub_dir), "Training Photo", sub_dir, id)


"""
Run:
"""
#init
SUB_KEY = '36fee94e28fa469fa8df5deec07c8f1c'
BASE_URL = 'https://westus.api.cognitive.microsoft.com/face/v1.0/'
PERSON_GROUP_ID = "known_persons"
CF.BaseUrl.set(BASE_URL)
CF.Key.set(SUB_KEY)

create_database("Known Persons", PERSON_GROUP_ID)
add_images("static/", PERSON_GROUP_ID)

