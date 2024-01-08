import pygame.font
from pygame.sprite import Group


# from kodanda import Kodanda

class Scoreboard:
    """ a class for scores display management """

    def __init__(self, rr_game):
        self.rr_game = rr_game
        self.settings = rr_game.settings
        self.screen = rr_game.screen
        self.screen_rect = self.screen.get_rect()
        self.stats = rr_game.stats

        # font colour and dimentions
        self.text_colour = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 40)

        self.stats.level = 1
        # self.kodandas = Kodanda()
        self.prep_score()
        self.prep_highscore()
        self.prep_level()
        self.displaying_the_hs_text()
        # self.prep_kodanda()

    def prep_score(self):
        """ as per the capabilities of pygame, scores need to be turne int rendered image"""
        score_string = str(self.stats.score)
        self.score_image = self.font.render(score_string, True, self.text_colour, self.settings.bg_color)

        # after rendering, create a rect at a position u wanna display the render
        # creating the score rect
        self.score_rect = self.screen.get_rect()
        # positioning the rect
        self.score_rect.right = self.screen_rect.right + 10
        self.score_rect.top = 20

        # score images (initially)

    def prep_level(self):
        """ turning the level into a rendered image"""
        self.lvl_str = str(self.stats.level)
        self.lvl_image = self.font.render(self.lvl_str, True, self.text_colour, self.settings.bg_color)

        # getting a rect for the render
        self.lvl_rect = self.screen.get_rect()
        # positioning the level rect jst below the score rect
        self.lvl_rect.centerx = self.screen_rect.centerx
        self.lvl_rect.top = self.score_rect.bottom - 20

    def prep_highscore(self):
        """getting a render for the high score"""
        self.hs_str = str(self.stats.highscore)
        self.hs_img = self.font.render(self.hs_str, True, self.text_colour, self.settings.bg_color)

        # rect of the high score image
        self.hs_rect = self.screen.get_rect()
        # positioning the gs rect
        self.hs_rect.left = self.screen_rect.left + 600
        # or
        # self.hs_rect.centerx = self.screen_rect.centerx
        self.hs_rect.top = self.screen_rect.top

    def update_highscore(self):
        """ displaying a new highscore if it's more """
        if self.stats.score > self.stats.highscore:
            self.stats.highscore = self.stats.score
            self.prep_highscore()

    def displaying_the_hs_text(self):
        """ displaying the 'Highscore' image text """
        self.hsimg_image = self.font.render('Highscore :', True, self.text_colour, self.settings.bg_color)
        self.hsimg_rect = self.screen.get_rect()
        # position
        self.hsimg_rect.left = self.screen_rect.left + 400
        self.hsimg_rect.top = self.screen_rect.top

    def display_scoreboard_methods(self):
        """ displaying the score, highscore and level """
        self.update_highscore()
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.hs_img, self.hs_rect)
        self.screen.blit(self.lvl_image, self.lvl_rect)
        self.screen.blit(self.hsimg_image, self.hsimg_rect)
        # self.kodandas.draw(self.screen)

