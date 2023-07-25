import random
import json

def load_location_data():
    with open('location_data.json') as file:
        location_data = json.load(file)
    return location_data

def location_mixer(location):
    location_data = load_location_data()

    if location in location_data:
        images = location_data[location]["images"]
        sounds = location_data[location]["sounds"]
        
        random_image = random.choice(images)
        random_sound = random.choice(sounds)
        
        return random_image, random_sound
    else:
        return None