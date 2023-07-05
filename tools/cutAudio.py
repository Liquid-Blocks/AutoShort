from moviepy.editor import AudioFileClip

input_file = "audio/birds.mp3"
output_file = "audio/birds_cut.mp3"
start_time = 0  # Start time in seconds
end_time = 15  # End time in seconds

# Load the audio clip
clip = AudioFileClip(input_file)

# Cut the audio clip
cut_clip = clip.subclip(start_time, end_time)

# Save the cut audio clip
cut_clip.write_audiofile(output_file)