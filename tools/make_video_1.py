from moviepy.editor import ImageClip, VideoFileClip, TextClip, CompositeVideoClip, vfx, AudioFileClip, CompositeAudioClip
from tools.utils import convert_text
from tools.location_mixer import location_mixer

# inputs
# text: Text to display 
# reaction_name: Name of the reaction vid
# location_image: Background image name
# location_audio: Audio over the video

def make_video(text, reaction_name, location):

    # Backgrounds and reactions paths (const)
    backgrounds_path = "src/backgrounds/"
    reactions_path = "src/reactions/"
    audio_path = "src/audio/"

    print("AutoShort - Mixing context")
    location_image, location_audio = location_mixer(location)

    # Load reaction video and remove green screen
    reaction = (VideoFileClip(reactions_path + reaction_name + ".gif", has_mask=True)
                .set_position(("right", "bottom")) # position of the reaction
                .set_duration(5)) # duration of reaction
    reaction = vfx.mask_color(reaction, color=reaction_params["color"], thr=15)

    #Load the background
    background = ImageClip(backgrounds_path + location_image + ".png", duration=reaction.duration)

    # Create text and position
    txt = TextClip(text, method='caption', font ="Arial-Bold", fontsize=100, size=(900, 1920) , color='white', stroke_color='black', stroke_width=5)
    txt = txt.set_position(('center', -400)).set_duration(reaction.duration)

    # Composite the video
    visual = CompositeVideoClip([background, reaction, txt])

    # Load audio file
    background_audio = (AudioFileClip(audio_path + location_audio + ".mp3")
            .subclip(0, reaction.duration))

    # Check if the reaction video has audio
    reaction_audio = reaction.audio
    if reaction_audio is not None:
        # Combine the reaction audio with the background audio
        audio = CompositeAudioClip([background_audio, reaction_audio])
    else:
        # Use only the background audio
        audio = background_audio

    final = visual.set_audio(audio)

    # Write to file with unique name

    final.write_videofile("results/"+ convert_text(text) + ".mp4", codec="libx264", fps=24)

    print("AutoShort - Video written to file.")