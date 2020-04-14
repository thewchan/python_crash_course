import sys
from time import sleep

import pygame
from pygame.sprite import Sprite

from settings import Settings
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from sideways_ship import SidewaysShip


class SidewaysShooter:
    """Over class to manage sideways shooter game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
            )
        pygame.display.set_caption("Sideways Shooter")
        self.stats = GameStats(self)
        self.sideways_ship = SidewaysShip(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            if self.stats.game_active:
                self.sideways_ship.update()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_DOWN:
            self.sideways_ship.moving_down = True
        elif event.key == pygame.K_UP:
            self.sideways_ship.moving_up = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_DOWN:
            self.sideways_ship.moving_down = False
        elif event.key == pygame.K_UP:
            self.sideways_ship.moving_up = False

    def _fire_bullet(self):
        """Creat a new bullet and add it to the bullets group."""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.right >= self.settings.screen_width:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions."""
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True,
            )
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()

    def _create_fleet(self):
        """Create the fleet of aliens."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_y = self.settings.screen_height - (2 * alien_height)
        number_aliens_y = available_space_y // (2 * alien_height)
        sideways_ship_width = self.sideways_ship.rect.width
        available_space_x = (
            self.settings.screen_width - (3 * alien_width) -
            sideways_ship_width
            )
        number_columns = available_space_x // (2 * alien_width) + 1
        for column_number in (range(1, number_columns)):
            for alien_number in range(number_aliens_y):
                self._create_alien(alien_number, column_number)

    def _create_alien(self, alien_number, column_number):
        """Create an alien and place it in the row."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.y = alien_height + 2 * alien_height * alien_number
        alien.rect.y = alien.y
        alien.rect.x = (
            self.settings.screen_width - 2 * alien_width * column_number
            )
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """
        Move the entire fleet towards the sideways ship
            and change the fleet's direction.
        """
        for alien in self.aliens.sprites():
            alien.rect.x -= self.settings.fleet_approach_speed
        self.settings.fleet_direction *= -1

    def _check_aliens_leftmost_edge(self):
        """Check if any aliens have reached the leftmost edge of the screen."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.left <= screen_rect.left:
                self._sideways_ship_hit()
                break

    def _update_aliens(self):
        """
        Check if the fleet is at an edge,
            then update the positions of all aliens in the fleet.
        """
        self._check_fleet_edges()
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.sideways_ship, self.aliens):
            self._sideways_ship_hit()
        self._check_aliens_leftmost_edge()

    def _sideways_ship_hit(self):
        """Respond to the sideways ship being hit by an alien."""
        if self.stats.sideways_ships_left > 0:
            self.stats.sideways_ships_left -= 1
            self.aliens.empty()
            self.bullets.empty()
            self._create_fleet()
            self.sideways_ship.center_sideways_ship()
            sleep(0.5)
        else:
            self.stats.game_active = False

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.sideways_ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        pygame.display.flip()


if __name__ == '__main__':
    sws = SidewaysShooter()
    sws.run_game()
