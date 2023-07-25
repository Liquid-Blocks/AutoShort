from tools.make_video import make_video
from tools.get_completion import get_completion
from tools.get_chat_completion import get_chat_completion
from tools.location_mixer import location_mixer
from tools.utils import convert_text
import json

params = {
    "confused-travolta": { "color": [20,189,0], "threshold": 15, "extension": ".mp4"},
    "jonah-jameson-laughing": { "color": [0,255,0], "threshold": 15, "extension": ".mp4"},
    "breaking-bad-i-am-the-danger": { "color": [0,255,0], "threshold": 15, "extension": ".mp4"},
    "patrick-bateman-sigma-face": { "color": [0,255,0], "threshold": 15, "extension": ".mp4"},
    "shaq-hot-ones-surprised": { "color": [19,255,8], "threshold": 15, "extension": ".gif"}
}

print("AutoShort - Reading promt file.")
with open("./prompts/prompt.txt", "r") as file:
    # Read the text from the file
    prompt = file.read()

print("AutoShort - Call openAi completion.")
result = get_chat_completion(prompt)
print(result)
if result.get('statusCode') == 200:
    # Extract the JSON content from the body
    body_content = json.loads(result['body'])
    print(body_content)
else:
    print("Error:", result.get('statusCode'))

location = body_content["location"].lower().replace(" ", "-")
reaction = body_content["reaction"].lower().replace(" ", "-")

print("AutoShort - Mixing context")
location_image, location_audio = location_mixer(location) 

print("AutoShort - Launching video creation process...")
# Prepare the parameters
params = {
    "text": body_content["text"],
    "reaction_name": reaction,
    "reaction_params": params[reaction],
    "background_name": location_image,
    "background_audio_name": location_audio,
    "explanations": body_content["explanations"]
}

# Write parameters to a JSON file
with open("video_templates/" + convert_text(body_content["text"]) + ".json", "w") as file:
    json.dump(params, file)

# Call the make_video function
make_video(**params)

print("AutoShort - Video created successfully!")