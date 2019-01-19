import cognitive_face as CF

"""
2019 Cruz Hacks
"""

#init
SUB_KEY = 'REPLACE'
BASE_URL = 'https://westus.api.cognitive.microsoft.com/face/v1.0/'
PERSON_GROUP_ID = "known_persons"
CF.BaseUrl.set(BASE_URL)
CF.Key.set(SUB_KEY)
    
# create Person Object
CF.person_group.create(PERSON_GROUP_ID, "Known Persons")

# now add a person
def add_person(name, user_data):
    response = CF.person.create(PERSON_GROUP_ID, name, user_data)

