from turtle import speed
from pytube import YouTube
import os
from pedalboard import Pedalboard, Reverb
from pedalboard.io import AudioFile
import slow
import shutil

def download(youtube_link):
  #youtube url
  yt = YouTube(youtube_link)
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
    #values should be 0.8 and 0.1
      Reverb(room_size=0.8, wet_level=0.1)
      ])
  print("Successfully added reverb.")

  # Run the audio through this pedalboard!
  effected = board(audio, samplerate)

  # Write the audio back as a wav file:
  with AudioFile('processed-output.wav', 'w', samplerate, effected.shape[0]) as f:
    f.write(effected)
  print("Successfully created new file.")

  #value should be 1.2
  slow.stretch('processed-output.wav', 1.2)
  print("Stretched song.")

  #delete unprocessed files
  os.remove('song.mp3')
  os.remove('processed-output.wav')
  print("Unprocessed files deleted.")

  #move file to folder on desktop
  curr_dir = os.getcwd()
  copy_path = "/Users/joebieker/Desktop"
  file_path = curr_dir + f"/stretched.wav"
  shutil.move(file_path, copy_path)
  print("File moved to desktop.")

  #rename file
  os.rename("/Users/joebieker/Desktop/stretched.wav", f"/Users/joebieker/Desktop/{yt.title}.wav")
