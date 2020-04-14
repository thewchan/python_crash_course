import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, sws_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = sws_game.screen
        self.settings = sws_game.settings
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.settings.screen_width - 2 * self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom or self.rect.top <= 0:
            return True

    def update(self):
        """moving the alien up or down."""
        self.y += (
            self.settings.alien_speed * self.settings.fleet_direction
            )
        self.rect.y = self.y
