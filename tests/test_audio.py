import sounddevice as sd
import numpy as np

def callback(indata, frames, time, status):
    if status:
        print(f"Audio status: {status}")
    print(indata[:10])  # Print first 10 samples

# Replace 'None' with the correct device index if needed
stream = sd.InputStream(callback=callback, channels=2, samplerate=44100, device=19)

stream.start()

input("Press Enter to stop...\n")
stream.stop()
