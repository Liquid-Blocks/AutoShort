from moviepy.editor import VideoFileClip, CompositeVideoClip, vfx, ColorClip

# Backgrounds and reactions paths (const)
reactions_path = "../src/reactions/"

# Load reaction video and remove green screen
reaction = (VideoFileClip(reactions_path + "shaq-hot-ones-surprised.mp4", has_mask=True)
            .set_position(("right", "bottom"))) # position of the reaction
            # .set_duration(5)) # duration of reaction
reaction = vfx.mask_color(reaction, color=[30,255,2], thr=0, s=1)

#Load the background
background = ColorClip(size=(1080, 1920), color=[255,255,255]).set_duration(reaction.duration)

# Composite the video
visual = CompositeVideoClip([background, reaction])


# Write to file with unique name

visual.write_videofile("result.mp4", codec="libx264", fps=24)

print("AutoShort - Video written to file.")