import pygame.font

class Button:
    def __init__(self, rr_game, text):

        # basic overview/requirements of the "button" class:
        # initialization, button rect attributes - dimensions, colour . , Position, custom text printing.
        """ initializing the button rect """
        self.screen = rr_game.screen
        self.screen_rect = self.screen.get_rect()

        # setting the dimensions of the rect initialized on the screen
        self.width, self.height = 100, 25

        # building the rect
        self.rect = pygame.Rect( 0 , 0 , self.width, self.height)
        self.rect.center = self.screen_rect.center

        # colour and font
        self.button_colour = (255, 255, 255)
        self.text_colour = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 34, bold = 1)

        # text to be displayed once in the game
        self._display_text(text)

    def _display_text(self, text):
        """ rendering the text_image and placing on the button at the centre"""
        # .render(text, antialias, colour, rect colour)
        self.text_image = self.font.render(text, True, self.text_colour, self.button_colour )

        # since image a surface, it needs a rect too
        self.text_image_rect = self.text_image.get_rect()
        # positioning the text image rect right on the top of the button rect
        self.text_image_rect.center = self.rect.center # the button rect

    def drawing_button_on_screen(self):
        """ drawing the button rect onto the screen """
        self.screen.fill(self.button_colour, self.rect)
        # screen.fill() method is used to fill a surface (e.g., a screen or a rectangle) with a specified color
        # it takes to attributes, the colour( a tuple ) and the rect, the rectangular area to be filled with the specified color
        self.screen.blit(self.text_image, self.text_image_rect) # blit.() takes the "image" and "rect"

