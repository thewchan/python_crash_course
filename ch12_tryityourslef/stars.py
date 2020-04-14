import sys

import pygame
from pygame.sprite import Sprite


class StarField:
    """Overall class for a star field."""

    def __init__(self):
        """Initialize the game and background resources."""
        pygame.init()
        self.screen_width = 1200
        self.screen_height = 800
        self.screen = pygame.display.set_mode((
            self.screen_width, self.screen_height
            ))
        pygame.display.set_caption("Star Field")
        self.bg_color = (0, 0, 0)
        self.stars = pygame.sprite.Group()
        self._creat_starfield()

    def _creat_starfield(self):
        """Create a field of stars."""
        star = Star(self)
        star_width, star_height = star.rect.size
        available_space_x = self.screen_width - (2 * star_width)
        number_stars_x = available_space_x // (2 * star_width)
        available_space_y = self.screen_height - 2 * star_height
        number_rows = available_space_y // (2 * star_height)
        for row_number in range(number_rows):
            for star_number in range(number_stars_x):
                self._creat_star(star_number, row_number)

    def _creat_star(self, star_number, row_number):
        """Create a star and place in the row."""
        star = Star(self)
        star_width, star_height = star.rect.size
        star.x = star_width + 2 * star_width * star_number
        star.rect.x = star.x
        star.rect.y = star.rect.height + 2 * star.rect.height * row_number
        self.stars.add(star)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()
            self.screen.fill(self.bg_color)
            self.stars.draw(self.screen)
            pygame.display.flip()


class Star(Sprite):
    """Class to represent a star."""

    def __init__(self, sf_game):
        """Initialize the star and set its starting position."""
        super().__init__()
        self.screen = sf_game.screen
        self.image = pygame.image.load('star.jpg')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)


if __name__ == '__main__':
    sf = StarField()
    sf.run_game()
