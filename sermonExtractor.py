# I just wanted to grab the lastest sermon from my church and extract the audio.
#  This grabs the audio, converts to mp3 and only includes the start of the sermon until the end.
#
import pytube
import os
import subprocess
import datetime
from pytube import YouTube
from pytube.cli import on_progress
from sys import argv
from pydub import AudioSegment

# For the Usage portion below to spit out the current name of the script.
script_name = os.path.basename(__file__)

# Get the current date in MM-DD-YYYY format
current_date = datetime.datetime.now().strftime("%m-%d-%Y")

# Validate command line arguments
if len(argv) != 4:
     print("Usage: " + script_name + " <YouTube link> Start Time HH:MM:SS Duration Time HH:MM:SS")
     exit(1)

# Selecting portion we want to cut
start_time = argv[2]
duration = argv[3]

link = argv[1]
# Set to download file to the current directory
dldir = os.getcwd()

# Initialize YouTube object with the provided link and get metadata about the video
yt = YouTube(link, on_progress_callback=on_progress)
print("Title: ", yt.title)
print("Channel Name: ", yt.author)
print("Views: ", yt.views)

# Download audio stream and save it to disk
audio_streams = yt.streams.filter(only_audio=True)
audio_stream = audio_streams.first()
audio_filename = audio_stream.download(output_path=dldir)

# Rename the audio file to a standardized name
base, ext = os.path.splitext(audio_filename)
new_file = f"BGA_{current_date}.mp4"
output_file = f"BGA_{current_date}.mp3"
trimmed_file = f"Trimed_BGA_{current_date}.mp3"
os.rename(audio_filename, new_file)

# Run ffmpeg to convert the audio file to mp3 format
subprocess.call(['ffmpeg', '-i', new_file, '-vn', '-acodec', 'libmp3lame', '-b:a', '128k', output_file])

# Extract the desired section of the input audio file
subprocess.call(['ffmpeg', '-i', output_file, '-ss', str(start_time), '-t', str(duration), '-vn', '-c:a', 'copy', trimmed_file])

# Remove the original downloaded file
os.remove(new_file)

# Notify the user that the script has finished executing
print("Audio extraction complete!")
