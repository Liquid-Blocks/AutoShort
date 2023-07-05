from moviepy.editor import ImageClip, VideoFileClip, TextClip, CompositeVideoClip, vfx, AudioFileClip, CompositeAudioClip

print("launching video creation process")

# Backgrounds and reactions paths
backgrounds_path = "src/backgrounds/"
reactions_path = "src/reactions/"
audio_path = "src/audio/"

# Load reaction video and remove green screen
reaction = (VideoFileClip(reactions_path + "j-jonah-jameson-laughing.mp4", has_mask=True)
            .set_position(("right", "bottom")) # position of the reaction
            .set_duration(5)) # duration of reaction
reaction = vfx.mask_color(reaction, color=[0,255,0], thr=15)

#Load the background
background = ImageClip(backgrounds_path + "terrain.png", duration=reaction.duration)

# Create text and position
txt = TextClip("When your friend claims he can outdrive you and then tops it 10 yards.", method='caption', font ="Arial-Bold", fontsize=100, size=(900, 1920) , color='white', stroke_color='black', stroke_width=5)
txt = txt.set_position(('center', -400)).set_duration(reaction.duration)

# Composite the video
visual = CompositeVideoClip([background, reaction, txt])

# Load audio file
background_audio = (AudioFileClip(audio_path + "birds.mp3")
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

# Write to file
final.write_videofile(f"results/output_video.mp4", codec="libx264", fps=24)

print("Video created successfully!")