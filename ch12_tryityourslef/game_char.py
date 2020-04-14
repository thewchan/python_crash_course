import sys

import pygame

from lotus import Lotus

class LotusCenter:
    """Lotus in the middle of a white screen."""

    def __init__(self):
        """Initiate game and needed resources."""
        pygame.init()

        self.screen = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("Lotus in the Center")
        
        self.bg_color = (255, 255, 255)

        self.lotus = Lotus(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)
            self.lotus.blitme()
            pygame.display.flip()

if __name__ == '__main__':
    lotus_game = LotusCenter()
    lotus_game.run_game()