class Settings:
    """A class to store all settings for Sideway Shooters"""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # Sideway ship settings
        self.sideways_ship_speed = 1.5
        self.sideways_ship_limit = 3

        # Bullet settings.
        self.bullet_speed = 5
        self.bullet_width = 15
        self.bullet_height = 300
        self.bullet_color = (60, 60, 60)

        # Alien setting.
        self.alien_speed = 1.0
        self.fleet_approach_speed = 50
        # fleet_direction of 1 represents down; -1 represents up.
        self.fleet_direction = 1
