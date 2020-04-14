import sys

import pygame
from pygame.sprite import Sprite


class RainDrops:
    """Overall class for a raining screen."""

    def __init__(self):
        """Initialize the game and background resources."""
        pygame.init()
        self.screen_width = 1200
        self.screen_height = 800
        self.screen = pygame.display.set_mode((
            self.screen_width, self.screen_height
            ))
        pygame.display.set_caption("Rain Drops")
        self.bg_color = (255, 255, 255)
        self.raindrops = pygame.sprite.Group()
        self._creat_raining()

    def _creat_raining(self):
        """Create a raining screen."""
        raindrop = RainDrop(self)
        raindrop_width, raindrop_height = raindrop.rect.size
        available_space_x = self.screen_width - (2 * raindrop_width)
        number_raindrops_x = available_space_x // (2 * raindrop_width)
        available_space_y = self.screen_height - (2 * raindrop_height)
        number_rows = available_space_y // (2 * raindrop_height)
        for row_number in range(number_rows):
            for raindrop_number in range(number_raindrops_x):
                self._creat_raindrop(raindrop_number, row_number)

    def _creat_raindrop(self, raindrop_number, row_number):
        """Create a raindrop and place in the row."""
        raindrop = RainDrop(self)
        raindrop_width, raindrop_height = raindrop.rect.size
        raindrop.x = raindrop_width + 2 * raindrop_width * raindrop_number
        raindrop.y = (
            raindrop.rect.height + 2 * raindrop.rect.height * row_number
            )
        raindrop.rect.x = raindrop.x
        raindrop.rect.y = raindrop.y
        self.raindrops.add(raindrop)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            raindrop_count = -1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()
            for raindrop in self.raindrops.sprites():
                if raindrop.check_edges():
                    raindrop_count += 1
                    self._creat_raindrop(raindrop_count, 0)
                    self.raindrops.remove(raindrop)
            self.raindrops.update()
            self.screen.fill(self.bg_color)
            self.raindrops.draw(self.screen)
            pygame.display.flip()


class RainDrop(Sprite):
    """Class to represent a raindrop."""

    def __init__(self, rd_game):
        """Initialize the star and set its starting position."""
        super().__init__()
        self.raindrops_speed = 1
        self.screen = rd_game.screen
        self.image = pygame.image.load('raindrop.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.y = float(self.rect.y)

    def update(self):
        """Move raindrop downwards."""
        self.y += self.raindrops_speed
        self.rect.y = self.y

    def check_edges(self):
        """Return True if raindrop is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom:
            return True


if __name__ == '__main__':
    rd = RainDrops()
    rd.run_game()
