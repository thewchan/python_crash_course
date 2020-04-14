class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, sws_game):
        """Initialize statistics."""
        self.settings = sws_game.settings
        self.reset_stats()
        self.game_active = True

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.sideways_ships_left = self.settings.sideways_ship_limit
