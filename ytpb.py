from turtle import speed
from pytube import YouTube
import os
from pedalboard import Pedalboard, Reverb
from pedalboard.io import AudioFile
import slow

#youtube url
yt = YouTube(str(input("Enter URL of youtube video: \n ")))
video = yt.streams.filter(only_audio=True).first()

#sets destination as current directory
destination = '.'
out_file = video.download(output_path=destination)

#renames to mp3 from mp4
new_file =  'song.mp3'
os.rename(out_file, new_file)
print(yt.title + " has been successfully downloaded.")



# Read in a whole audio file:
with AudioFile("song.mp3", 'r') as f:
  audio = f.read(f.frames)
  samplerate = f.samplerate

# Make a Pedalboard object, containing multiple plugins:
board = Pedalboard([
    Reverb(room_size=0.8, wet_level=0.1)
    ])
print("Successfully added reverb.")

# Run the audio through this pedalboard!
effected = board(audio, samplerate)

# Write the audio back as a wav file:
with AudioFile('processed-output.wav', 'w', samplerate, effected.shape[0]) as f:
  f.write(effected)
print("Successfully created new file.")

slow.stretch('processed-output.wav', 1.2)
print("Stretched song.")

#delete unprocessed files
os.remove('song.mp3')
os.remove('processed-output.wav')
print("Unprocessed files deleted.")