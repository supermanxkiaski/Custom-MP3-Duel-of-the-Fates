from moviepy.editor import VideoFileClip, concatenate_videoclips, AudioFileClip, CompositeAudioClip
import numpy as np

# Load video
video = VideoFileClip(r"C:\Users\super\Desktop\Lightsaber Duel Custom MP3\duelofthefates.mp4")

# Load audio
audio = AudioFileClip(r"C:\Users\super\Desktop\Lightsaber Duel Custom MP3\sound.mp3")

# Manually created list of times when lightsabers clash
clash_times = [1.75, 3.55, 5.29, 5.45, 9.00, 10.72, 11.67, 11.89, 12.60, 13.20, 13.45, 13.70, 14.20, 15.15, 15.40, 15.75, 16.06, 21.00, 22.00, 23.40,
    25.00,
    25.50,
    27.50,
    31.80,
    32.00,
    33.50,
    34.00,
    35.20,
    35.75,
    36.35,
    37.50,
    49.00,
    54.00,
    56.00,
    58.00,
    59.00,
    60.00,
    62.00,
    68.50,
    69.00,
    75.00,
    76.50,
    78.40,
    80.00,
    80.50,
    81.75,
    87.90,
    89.00,
    90.70,
    93.00,
    93.30,
    95.00,
    96.15,
    97.00,
    98.50,
    105.00,
    118.30,
    138.00,
    140.50,
    141.75,
    142.30,
    142.75,
    147.50,
    148.00,
    148.45,
    153.75,
    154.00,
    155.00,
    156.10,
    159.50,
    160.00,
    161.00,
    162.10,
    167.25,
    167.50,
    168.53,
    170.00,
    171.50,
    172.00,
    189.00,
    189.25,
    189.50,
    192.00,
    193.00,
    193.50,
    194.00,
    194.30,
    195.00,
    195.25,
    196.00,
    197.00,
    197.40,
    197.75,
    198.60,
    199.00,
    199.40,
    199.65,
    202.00,
    202.60,
    203.50,
    204.00,
    205.00,
    205.10,
    206.00,
    207.00,
    208.00,
    208.60,
    214.50,
    215.00,
    215.50,
    223.50,
    224.00,
    225.00,
    226.05,
    226.60,
    227.50,
    230.00,]  # replace with your times

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
