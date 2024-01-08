# Ramrajya

import sys
import pygame
from settings import Settings
from kodanda import Kodanda
from ramastra import Ramastra
from danav import Danav
from start_button import Button
from game_stats import GameStats
from scoreboard import Scoreboard as sb

# clean code
class Ramrajya:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Ramrajya: slay the evil")

        self.kodanda = Kodanda(self)
        self.ramastras = pygame.sprite.Group()
        # self.ramastra = pygame.sprite.group() - error
        self.danavas = pygame.sprite.Group()
        self.stats = GameStats(self)
        # self.button = Button()
        self.start_button = Button(self, "START")  # instance of the Button class
        self._create_Sena()
        self.sb = sb(self)
        # Game is active or not depending upon fatal collisions
        self.game_on = False


    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if self.game_on:
                self._update_ramastra()
                self.kodanda.update()
                self._update_danavas()
            if not self.game_on:
                pygame.mouse.set_visible(True)
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
            # mouse click response on the play button
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                self._check_start_button(mouse_position)

    def _check_start_button(self, mouse_position):
        """ method to start the game after the player hits start button """
        click = self.start_button.rect.collidepoint(mouse_position)
        if click and not self.game_on:
            # initializing the dynamic game settings
            self.settings.init_dynamic_settings()
            # restarting the game
            self.stats.reset_stats()
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_highscore()
            self.game_on = True

            # vanishing any visible surface, rect , object for the new game
            self.ramastras.empty()
            self.danavas.empty()

            # updating the danav sena and the bow for the new game at their og position
            self._create_Sena()
            self.kodanda.reappear_kodanda()

            # hiding th mouse button called by the pygame event above
            pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.kodanda.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.kodanda.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_ramastra()

    def _check_keyup_events(self, event):
        # """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.kodanda.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.kodanda.moving_left = False

    def _fire_ramastra(self):
        """Create a new arrow and add it to the Ramastra group."""
        if len(self.ramastras) < self.settings.ramastras_allowed:
            new_ramastra = Ramastra(self)
            self.ramastras.add(new_ramastra)

    def _update_ramastra(self):
        # updating the position of ramastras and get rid of old ones
        self.ramastras.update()
        # deleting disappeared arrows
        for arrows in self.ramastras.copy():
            if arrows.rect.bottom <= 0:
                self.ramastras.remove(arrows)
        self._check_collisions()

    def _check_collisions(self):
        """ collision response """
        # removing any rect that has collided
        collisions = pygame.sprite.groupcollide(self.ramastras, self.danavas, True, True)
        if collisions:
            for danvas in collisions.values():
                self.stats.score += self.settings.danav_points * len(danvas)
            self.sb.prep_score()
            self.sb.prep_highscore()

        if not self.danavas:
            self.ramastras.empty()
            self._create_Sena()
            #
            self.settings.speed_increament()
            # increasing the level gradually after danavas get hit and player scores
            self.stats.level += 1
            self.sb.prep_level()

    def _kodanda_hit(self):
        """Respond to Bow being hit by an alien."""
        if self.stats.kodanda_left > 0:
            # decreasing the no of Bow's left (analogous to life on games) .
            self.stats.kodanda_left -= 1
            # Get rid of arrows and danavas on screen after collision.
            self.ramastras.empty()
            self.danavas.empty()
            # Create a new fleet and center the ship.
            self._create_Sena()
            self.kodanda.reappear_kodanda()
        else:
            self.game_on = False

    def _update_danavas(self):
        """Update the positions of all danavas in the sena."""
        """Check if the sena is at an edge, then update positions."""
        self._check_sena_ke_edges()
        self.danavas.update()

        # verifying collision either between kodanda and any danava
        if pygame.sprite.spritecollideany(self.kodanda, self.danavas):
            self._kodanda_hit()

        # or the bottom edge and the danava
        self._check_danav_bottomedge()

    def _check_danav_bottomedge(self):
        # checking if any danava has reached the bottom
        for danav in self.danavas.sprites():
            if danav.rect.bottom >= self.settings.screen_height:
                self._kodanda_hit()
                break

    def _create_Sena(self):
        danav = Danav(self)
        danav_width, danav_height = danav.rect.size

        current_x, current_y = danav_width, danav_height
        while current_y < (self.settings.screen_height - 4 * danav_height):
            while current_x < (self.settings.screen_width - danav_width):
                self._create_danav(current_x, current_y)
                current_x += 2 * danav_width

            # Finished a row; reset x value, and increment y value.
            current_x = danav_width
            current_y += 2 * danav_height

    def _create_danav(self, on_x, on_y):
        new_danav = Danav(self)
        new_danav.x = on_x
        new_danav.rect.x = on_x
        new_danav.rect.y = on_y
        self.danavas.add(new_danav)

    def _check_sena_ke_edges(self):
        """Respond appropriately if any danav have reached an edge."""
        for danav1 in self.danavas.sprites():
            if danav1.check_edges():
                self._change_sena_ki_direction()
                break

    def _change_sena_ki_direction(self):
        """Drop the entire sena and change the sena's direction."""
        for danav in self.danavas.sprites():
            danav.rect.y += self.settings.sena_down_speed
        self.settings.sena_direction *= -1

    def _update_screen(self):
        #    """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        # self.ramastra.blitme()
        for ramastra2 in self.ramastras:
            ramastra2.blitme()
        self.kodanda.blitme()
        self.danavas.draw(self.screen)
        # Make the most recently drawn screen visible.
        # updating the screen with the play button as soon as kodanda limit leads the game_on = false
        if not self.game_on:
            self.start_button.drawing_button_on_screen()
        self.sb.display_scoreboard_methods()
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    rr = Ramrajya()
    rr.run_game()