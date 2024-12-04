from src.real_time import RealTimeAudio
from src.visualizer import Visualizer
import pygame
import numpy as np

def main():
    # Initialize real-time audio and visualizer
    visualizer = Visualizer(width=800, height=400)
    audio = RealTimeAudio(sample_rate=44100, block_size=1024)

    def audio_callback(audio_data):
        """Callback function to pass audio data to visualizer."""
        # Normalize audio data for better visuals
        normalized_data = audio_data / np.max(audio_data)
        visualizer.draw_bars(normalized_data)

    audio.callback = audio_callback
    audio.start_stream()

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    # Clean up
    audio.stop_stream()
    pygame.quit()

if __name__ == "__main__":
    main()
