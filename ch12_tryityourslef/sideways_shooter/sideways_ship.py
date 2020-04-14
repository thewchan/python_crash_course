import pygame
from pygame.sprite import Sprite


class SidewaysShip:
    """A class to manage the sideways ship."""

    def __init__(self, sws_game):
        """Initialize the ship and set its starting position."""
        self.screen = sws_game.screen
        self.settings = sws_game.settings
        self.screen_rect = sws_game.screen.get_rect()
        self.image = pygame.image.load('images/sideways_ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.midleft = self.screen_rect.midleft
        self.moving_down = False
        self.moving_up = False
        self.y = float(self.rect.y)

    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.sideways_ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.sideways_ship_speed
        self.rect.y = self.y

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_sideways_ship(self):
        """Center the sideways ship on the screen."""
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)
