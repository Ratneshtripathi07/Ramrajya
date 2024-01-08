class GameStats:
    """ Track statistics for the game"""

    def __init__(self, rr_game):
        """ initialize the statistics for the game"""
        self.settings = rr_game.settings
        self.reset_stats()

        # score starting
        self.highscore = 0


    def reset_stats(self):
        self.kodanda_left = self.settings.kodanda_limit
        self.score = 0
        self.level = 1



