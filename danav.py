# Danav is the enemy in the
import  pygame
from pygame.sprite import Sprite
from settings import Settings

class Danav(Sprite):
    """ Initiating the class for single Danav """
    def __init__(self, rr_game):
        """ above is the initialization of the danav's starting position"""
        super().__init__()
        self.screen = rr_game.screen
        # self.image = pygame.image.load("images/Demon3 (Custom).png")
        self.image = pygame.image.load("images/Demon5.png")
        self.rect = self.image.get_rect()
        # starting the danav at top left of the screen
        self.settings = rr_game.settings

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # exact position
        self.x = float(self.rect.x)

    def check_edges(self):
        """ Return True if any danav rect is at edge of screen."""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

    def update(self):
        """Moving the danav left/right."""
        self.x += self.settings.danav_speed * self.settings.sena_direction
        self.rect.x = self.x

        # showing the danav on screen
    # def blitme(self):
    #     """Draw the danav at its current location."""
    #     self.screen.blit(self.image, self.rect)

