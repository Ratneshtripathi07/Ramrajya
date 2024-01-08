import pygame
from pygame.sprite import Sprite

class Ramastra(Sprite):
    """A class to manage ramastras fired from the ship."""

    def __init__(self, rr_game):
        """Create a ramastra object at the ship's current position."""
        super().__init__()
        self.screen = rr_game.screen
        self.settings = rr_game.settings

        # Load the ramastra image
        self.image = pygame.image.load('images/Ramastra2.png')
        self.rect = self.image.get_rect()

        # Set the initial position of the ramastra to be at the ship's position.
        self.rect.midtop = rr_game.kodanda.rect.midtop

        # Store the ramastra's position as a float.
        self.y = float(self.rect.y)

    def update(self):
        """Move the ramastra up the screen."""
        # Update the exact position of the ramastra.
        # since the 0,0 is at left top corner and both axes are positive, so, moving up from the bottom is actually moving towards y=0 i.e., decrease
        self.y -= self.settings.ramastra_speed
        # Update the rect position.
        self.rect.y = self.y

    def blitme(self):
        """Draw the ramastra to the screen."""
        self.screen.blit(self.image, self.rect)
