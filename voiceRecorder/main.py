import pyaudio
import wave
from time import time

# ------------------------ Open audio and read the stream ----------------------------
audio = pyaudio.PyAudio()
stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)

# ------------------------ Keep track of the stream ----------------------------
frames = []
try:
    while True:
        data = stream.read(1024)
        frames.append(data)
except KeyboardInterrupt:
    pass

# ------------------------ Stop recording ----------------------------
stream.stop_stream()
stream.close()
audio.terminate()

# ------------------------ Set the file names ----------------------------
timeNow = time()
timeNow = str(timeNow).split('.')
timeNow = timeNow[0] + timeNow[1]

# ------------------------ Save the recordings ----------------------------
soundfile = wave.open(f"recordings/{timeNow}.wav", 'wb')
soundfile.setnchannels(1)
soundfile.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
soundfile.setframerate(44100)
soundfile.writeframes(b"".join(frames))
soundfile.close()


