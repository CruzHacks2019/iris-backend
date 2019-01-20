from APIClient import *
"""
2019 Cruz Hacks
"""
client = APIClient("people_13")
client.create_database("Known Users")
client.add_person("Tejas", "your grandson who doesn't need sleep", "static/tejas/*.jpg", "Tejas goes to Diablo Valley College and has been to over 40 hackathons.")
client.add_person("Andrew", "your annoying friend who goes to UCSC", "static/andrew/*.jpg", "Andrew was born in Santa Cruz but grew up in Silicon Valley. He likes building robots and reading the changelog for new Python features.")
client.add_person("Stewart", "your grandchild who likes to hack on hardware", "static/stewart/*.jpg", "Stewart is your grandchild who lives in Los Angeles. He likes to come over to see you and help you mow your lawn.")
client.add_person("Egypt", "your friend who helps you get groceries", "static/egypt/*.jpg", "Egypt is your friend that has good hair and user experience skills.")
client.add_person("Torin", "your grandson who lives in Marina", "static/torin/*.jpg", "Torin is your grandson who is a teaching assistant at CSUMB.")
client.train_data()
client.print_status()
client.print_list()