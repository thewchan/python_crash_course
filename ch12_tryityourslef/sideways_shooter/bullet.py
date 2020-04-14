import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, sws_game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = sws_game.screen
        self.settings = sws_game.settings
        self.color = self.settings.bullet_color
        self.rect = pygame.Rect(
            0, 0, self.settings.bullet_width, self.settings.bullet_height
            )
        self.rect.midright = sws_game.sideways_ship.rect.midright
        self.x = float(self.rect.x)

    def update(self):
        """Move the bullet across to the right of the screen."""
        self.x += self.settings.bullet_speed
        self.rect.x = self.x

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)