import wave

def stretch( fname,  factor ):
 ''' Stretches the audio in fname by the factor'''
 infile=wave.open( fname, 'rb')
 rate= infile.getframerate()
 channels=infile.getnchannels()
 swidth=infile.getsampwidth()
 nframes= infile.getnframes()
 audio_signal= infile.readframes(nframes)
 outfile = wave.open('stretched.wav', 'wb')
 outfile.setnchannels(channels)
 outfile.setsampwidth(swidth)
 outfile.setframerate(rate/factor)
 outfile.writeframes(audio_signal)
 outfile.close()
 return;
