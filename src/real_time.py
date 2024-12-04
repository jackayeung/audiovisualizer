import sounddevice as sd
import numpy as np

class RealTimeAudio:
    def __init__(self, callback=None, sample_rate=44100, block_size=1024):
        self.sample_rate = sample_rate
        self.block_size = block_size
        self.callback = callback
        self.audio_data = np.zeros(block_size)

    def audio_callback(self, indata, frames, time, status):
        """Process audio input in real-time."""
        if status:
            print(f"Audio status: {status}")  # Log the overflow for debugging
            return  # Skip this frame if overflow occurs
        self.audio_data = np.abs(indata[:, 0])  # Extract mono channel
        if self.callback:
            self.callback(self.audio_data)

    def start_stream(self):
        """Start the audio stream."""
        self.stream = sd.InputStream(
            channels=1,
            samplerate=self.sample_rate,
            blocksize=self.block_size,
            callback=self.audio_callback
        )
        self.stream.start()

    def stop_stream(self):
        """Stop the audio stream."""
        self.stream.stop()
        self.stream.close()
