import sys
import os
import pytest
import sounddevice as sd
import numpy as np
from src.real_time import RealTimeAudio

# Add project root to PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

def test_audio_devices():
    """Test if audio devices are listed properly."""
    devices = sd.query_devices()
    assert len(devices) > 0, "No audio devices found."

def test_audio_callback():
    """Test if the audio callback receives valid audio data."""
    def mock_callback(audio_data):
        assert isinstance(audio_data, np.ndarray), "Audio data is not a numpy array."
        assert len(audio_data) > 0, "Audio data is empty."
        assert np.all(audio_data >= 0), "Audio data contains invalid values."

    audio = RealTimeAudio(callback=mock_callback, sample_rate=44100, block_size=1024)
    audio.audio_callback(np.random.rand(1024, 1), None, None, None)  # Mock input data
