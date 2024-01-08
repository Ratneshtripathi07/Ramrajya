import pygame

class Kodanda:
    """A class to manage the kodanda."""

    def __init__(self, rr_game):
        """Initialize the kodanda and set its starting position."""
        self.screen = rr_game.screen
        ##
        self.settings = rr_game.settings
        self.screen_rect = rr_game.screen.get_rect()

        # Load the kodanda image and get its rect.
        self.image = pygame.image.load('images/Bow.png')
        self.rect = self.image.get_rect()

        # Start each new kodanda at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        ##
        # Storing a float for the kodanda's exact horizontal position.
        self.x = float(self.rect.x)

        # Movement flags; start with a kodanda that's not moving.
        self.moving_right = False
        self.moving_left = False

    def reappear_kodanda(self):
        """ after collision, reappear the Bow untill the game overs"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def update(self):
        """Update the kodanda's position based on movement flags."""
        # Update the kodanda's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.kodanda_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.kodanda_speed

        # Update rect object from self.x.
        self.rect.x = self.x

    def blitme(self):
        """Draw the kodanda at its current location."""
        self.screen.blit(self.image, self.rect)
