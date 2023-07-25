from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

# Replace 'input.mp4' with the path to your input file
input_file = 'input.mp4'
output_file = 'output.mp4'

# Set the start and end times in seconds
start_time = 0
end_time = 5

# Extract the subclip using MoviePy's ffmpeg_extract_subclip function
ffmpeg_extract_subclip(input_file, start_time, end_time, targetname=output_file)