import cognitive_face as CF
from PIL import Image
import glob
import time
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
    for img in glob.glob(img_dir):
        
        #print(img)
        CF.person.add_face(img, id, person_id)
    

    #print(CF.person_group.get_status(id))

def add_images(directory, id):
    for sub_dir in glob.glob(directory):
        add_person(str(sub_dir), "Training Photo", sub_dir, id)


"""
Run:
"""
#init
SUB_KEY = '36fee94e28fa469fa8df5deec07c8f1c'
BASE_URL = 'https://westus.api.cognitive.microsoft.com/face/v1.0/'
PERSON_GROUP_ID = "people_two"
CF.BaseUrl.set(BASE_URL)
CF.Key.set(SUB_KEY)

create_database("Known Persons", PERSON_GROUP_ID)
add_person("tejas", "Training", "static/tejas/*.jpg", PERSON_GROUP_ID)
add_person("andrew", "Training", "static/andrew/*.jpg", PERSON_GROUP_ID)
CF.person_group.train(PERSON_GROUP_ID)

time.sleep(5)
response = CF.person_group.get_status(PERSON_GROUP_ID)
status = response['status']
print(status)
print(CF.person.lists(PERSON_GROUP_ID))
