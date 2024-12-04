import sounddevice as sd
import numpy as np

class RealTimeAudio:
    def __init__(self, callback=None, sample_rate=44100, block_size=1024, device=19):
        self.sample_rate = sample_rate
        self.block_size = block_size
        self.callback = callback
        self.device = device
        self.audio_data = np.zeros(block_size)

    def audio_callback(self, indata, frames, time, status):
        if status:
            print(f"Audio status: {status}")  # Log overflow or other issues
            return

        # Combine left and right channels into one (mono)
        mono_data = np.mean(indata, axis=1)

        # Pass processed data to the user-defined callback
        self.audio_data = np.abs(mono_data)  # Use absolute values for visualization
        if self.callback:
            self.callback(self.audio_data)

    def start_stream(self):
        """Start the audio stream."""
        self.stream = sd.InputStream(
            channels=2,  # Stereo input
            samplerate=self.sample_rate,
            blocksize=self.block_size,
            device=self.device,
            callback=self.audio_callback
        )
        self.stream.start()

    def stop_stream(self):
        """Stop the audio stream."""
        self.stream.stop()
        self.stream.close()
