import pytest
import pygame
import numpy as np
from src.visualizer import Visualizer
import sys

def test_visualizer_initialization():
    """Test if the visualizer initializes correctly."""
    visualizer = Visualizer(width=800, height=400)
    assert visualizer.width == 800
    assert visualizer.height == 400

def test_draw_bars():
    """Test if the visualizer renders bars without errors."""
    visualizer = Visualizer(width=800, height=400)
    audio_data = np.random.rand(64)  # Generate random audio data
    try:
        visualizer.draw_bars(audio_data)  # Ensure no errors during rendering
    except Exception as e:
        pytest.fail(f"Visualizer failed with error: {e}")
