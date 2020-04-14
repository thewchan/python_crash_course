import sys

import pygame


class KeyLog:
    """Over class to manage key log program."""

    def __init__(self):
        """Initialize the key log program and resources."""
        pygame.init()
        self.screen = pygame.display.set_mode((300, 300))
        pygame.display.set_caption("Key Log")

    def run_game(self):
        """Satrt the main loop for the key log program."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    print(event.key)
            pygame.display.flip()


if __name__ == '__main__':
    kl = KeyLog()
    kl.run_game()
