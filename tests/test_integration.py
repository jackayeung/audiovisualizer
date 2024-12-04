import sys
import os
import pytest
import pygame
import numpy as np
from src.real_time import RealTimeAudio
from src.visualizer import Visualizer

# Add project root to PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

def test_audio_visualizer_integration():
    """Test the integration of audio input and visualizer."""
    visualizer = Visualizer(width=800, height=400)

    def mock_callback(audio_data):
        """Pass audio data to visualizer for rendering."""
        normalized_data = audio_data / np.max(audio_data)
        try:
            visualizer.draw_bars(normalized_data)  # Ensure visuals render without errors
        except Exception as e:
            pytest.fail(f"Visualizer failed during integration test: {e}")

    audio = RealTimeAudio(callback=mock_callback, sample_rate=44100, block_size=1024)
    try:
        # Simulate random audio input
        audio.audio_callback(np.random.rand(1024, 1), None, None, None)
    except Exception as e:
        pytest.fail(f"Audio input failed during integration test: {e}")
