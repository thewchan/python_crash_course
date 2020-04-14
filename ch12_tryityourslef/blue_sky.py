import sys

import pygame

class BlueSky:
    """Make a Pygame window with a blue background."""

    def __init__(self):
        """Initialize game window."""
        # Initialize pygame background settings.
        pygame.init()

        self.screen = pygame.display.set_mode((600, 400))
        pygame.display.set_caption("Blue Sky")

        # Set background color (RGB 0-255)
        self.bg_color = (0, 0, 255)

    def run_game(self):
        """Start main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #Redraw the screen during each pass through the loop.
            self.screen.fill(self.bg_color)

            # Make the most recently drawn screen visible.
            pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    bs = BlueSky()
    bs.run_game()

