import pygame

class Lotus:
    """A class for the lotus in the Lotus in the Center game."""

    def __init__(self, lotus_game):
        """Initialie the lotus and set its starting position."""
        self.screen = lotus_game.screen
        self.screen_rect = lotus_game.screen.get_rect()

        # Load the lotus image and get its rectangle.
        self.image = pygame.image.load('lotus.png')
        self.rect = self.image.get_rect()

        # Start each new ship at the center of the screen.
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw the lotus at its current location."""
        self.screen.blit(self.image, self.rect)