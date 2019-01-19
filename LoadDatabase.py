from APIClient import *
"""
2019 Cruz Hacks
"""
client = APIClient("people_three")
#client.create_database("Known Users")
client.add_person("Tejas", "Testing", "static/tejas/*.jpg")
client.add_person("Andrew", "Friend", "static/andrew/*.jpg")
client.train_data()
client.print_status()
client.print_list()