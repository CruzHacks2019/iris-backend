import cognitive_face as CF
import time
SUBSCRIPTION_KEY = '36fee94e28fa469fa8df5deec07c8f1c'
BASE_URL = 'https://westus.api.cognitive.microsoft.com/face/v1.0/'
PERSON_GROUP_ID = 'known-persons-test'
CF.BaseUrl.set(BASE_URL)
CF.Key.set(SUBSCRIPTION_KEY)

# CF.person_group.create(PERSON_GROUP_ID, 'Known Persons')

name = "Clemens Siebler"
user_data = 'More information can go here'
response = CF.person.create(PERSON_GROUP_ID, name, user_data)

# Get person_id from response
person_id = response['personId']

CF.person.add_face('static/tejas/tejas1.jpg', PERSON_GROUP_ID, person_id)

print(CF.person.lists(PERSON_GROUP_ID))

CF.person_group.train(PERSON_GROUP_ID)
time.sleep(15)


response = CF.person_group.get_status(PERSON_GROUP_ID)
status = response['status']
print(status)
