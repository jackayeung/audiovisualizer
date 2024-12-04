from src.real_time import RealTimeAudio
from src.visualizer import Visualizer
import pygame
import numpy as np

def main():
    # Initialize real-time audio and visualizer
    visualizer = Visualizer(width=800, height=400)
    audio = RealTimeAudio(sample_rate=22050, block_size=2048)

    def audio_callback(audio_data):
        # Scale the data to make it visually significant
        scaled_data = audio_data * 1000  # Amplify small values

        # Normalize the scaled data
        if np.max(scaled_data) > 0:
            normalized_data = scaled_data / np.max(scaled_data)
        else:
            normalized_data = scaled_data  # Prevent divide-by-zero errors

        # Debug the data being passed to the visualizer
        print(f"Normalized Data Min: {np.min(normalized_data)}, Max: {np.max(normalized_data)}")

        # Pass data to the visualizer
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
