import pygame
import numpy as np

class Visualizer:
    def __init__(self, width=800, height=400):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Real-Time Visualizer")
        self.width = width
        self.height = height

    def draw_bars(self, audio_data):
        """Draw frequency bars based on audio data."""
        self.screen.fill((0, 0, 0))  # Clear the screen
        num_bars = len(audio_data)
        bar_width = self.width // num_bars

        for i in range(num_bars):
            height = int(audio_data[i] * self.height)  # Scale data to screen height
            pygame.draw.rect(
                self.screen,
                (0, 255, 0),
                (i * bar_width, self.height - height, bar_width, height)
            )
        pygame.display.flip()
