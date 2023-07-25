from moviepy.editor import ImageClip, VideoFileClip, TextClip, CompositeVideoClip, vfx, AudioFileClip, CompositeAudioClip

import json
import sys
from tools.location_mixer import location_mixer
from tools.utils import convert_text

# Backgrounds and reactions paths (const)
backgrounds_path = "src/backgrounds/"
reactions_path = "src/reactions/"
audio_path = "src/audio/"

def read_json_file(file_path):
    # Open the file
    with open(file_path, 'r') as f:
        # Load JSON data from file
        data = json.load(f)
        return data
        

if __name__ == "__main__":
    # Check if the file name has been passed as a command line argument
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        data = read_json_file(file_path)
    else:
        print("Please provide a file path. Usage: python make.py <file_path>")

print("AutoShort - Received input")
print(data)

print("AutoShort - Mixing context")
location_image, location_audio = location_mixer(data["location"])

print("AutoShort - Load reaction data")
reaction_data = read_json_file(reactions_path+data["reaction"]+"/"+data["reaction"]+".json")

print("AutoShort - Load reaction video and remove green screen")
reaction = (VideoFileClip(reactions_path+data["reaction"]+"/"+data["reaction"]+".gif", has_mask=True)
            .set_position(("right", "bottom")) # position of the reaction
            .set_duration(reaction_data["length"])) # duration of reaction
reaction = vfx.mask_color(reaction, color=reaction_data["color"], thr=15)

print("AutoShort - Load the background image")
background = ImageClip(backgrounds_path + location_image + ".png", duration=reaction.duration)

print("AutoShort - Load the background audio")
background_audio = (AudioFileClip(audio_path + location_audio + ".mp3").subclip(0, reaction.duration))

if(reaction_data["has_audio"]):
    print("AutoShort - Load reaction audio")
    reaction_audio = (AudioFileClip(reactions_path+data["reaction"]+"/"+data["reaction"]+".mp3").subclip(0, reaction.duration))

    print("AutoShort - Composite audio")
    audio = CompositeAudioClip([background_audio, reaction_audio])
else:
    audio = background_audio

print("AutoShort - Create text and position")
txt = TextClip(data["text"], method='caption', font ="Arial-Bold", fontsize=100, size=(900, 1920) , color='white', stroke_color='black', stroke_width=5)
txt = txt.set_position(('center', -400)).set_duration(reaction.duration)

print("AutoShort - Composite video")
video = CompositeVideoClip([background, reaction, txt]).set_audio(audio)

# Write to file with unique name

video.write_videofile("results/"+ convert_text(data["text"]) + ".mp4", codec="libx264", fps=24)