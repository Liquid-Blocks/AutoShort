from moviepy.editor import AudioFileClip

def extract_audio(video_path, audio_path):
    video = AudioFileClip(video_path)
    video.audio.write_audiofile(audio_path)

video_path = './src/reactions/large-office.mp4'  # Input video file path
audio_path = 'output.mp3'  # Output audio file path

extract_audio(video_path, audio_path)