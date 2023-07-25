from tools.make_video import make_video
from tools.get_completion import get_completion
from tools.location_mixer import location_mixer
from tools.utils import convert_text
import json

reacts = {
    "confused-travolta": { "color": [20,189,0], "threshold": 15, "extension": ".mp4"},
    "jonah-jameson-laughing": { "color": [0,255,0], "threshold": 15, "extension": ".mp4"},
    "breaking-bad-i-am-the-danger": { "color": [0,255,0], "threshold": 15, "extension": ".mp4"},
    "patrick-bateman-sigma-face": { "color": [0,255,0], "threshold": 15, "extension": ".mp4"},
    "shaq-hot-ones-surprised": { "color": [19,255,8], "threshold": 15, "extension": ".gif"},
    "large-office": { "color": [61,255,3],  "threshold": 15, "extension": ".mp4", "reaction_audio": "the-office-no-god.mp3"}
}

body_content = {
    "location": "on-the-green",
    "reaction": "large-office",
    "text": "When you finally get that birdie putt, but then you count again...",
    "explanations": ""
}

location = body_content["location"].lower().replace(" ", "-")
reaction = body_content["reaction"].lower().replace(" ", "-")

print("AutoShort - Mixing context")
location_image, location_audio = location_mixer(location) 

print("AutoShort - Launching video creation process...")
# Prepare the parameters
params = {
    "text": body_content["text"],
    "reaction_name": reaction,
    "reaction_params": reacts[reaction],
    "background_name": location_image,
    "background_audio_name": location_audio,
    "explanations": body_content["explanations"]
}

# Call the make_video function
make_video(**params)

print("AutoShort - Video created successfully!")