from moviepy.editor import VideoFileClip, concatenate_videoclips, AudioFileClip, CompositeAudioClip
import numpy as np

# Load video
video = VideoFileClip(r"C:\Users\super\Desktop\Lightsaber Duel Custom MP3\lightsaber_duel.mp4")

# Load audio
audio = AudioFileClip(r"C:\Users\super\Desktop\Lightsaber Duel Custom MP3\sound.mp3")

# Manually created list of times when lightsabers clash
clash_times = [1.63, 3.37, 5.29, 5.45, 9.00, 10.72, 11.67, 11.89, 12.60, 13.20, 13.45, 13.70, 14.20, 15.15, 15.40, 15.75, 16.06, ]  # replace with your times

# Create a list to hold the audio clips
audio_clips = []

# Loop through the clash times
for i in range(len(clash_times)):
    # Add the sound effect at this clash time
    audio_clips.append(audio.set_start(clash_times[i]))

# Create a composite audio clip that includes the sound effects at the specified times
composite_audio = CompositeAudioClip(audio_clips)

# Set the audio of the video to the new composite audio
final_clip = video.set_audio(composite_audio)

# Write the result to a file
final_clip.write_videofile(r"C:\Users\super\Desktop\Lightsaber Duel Custom MP3\output.mp4")
