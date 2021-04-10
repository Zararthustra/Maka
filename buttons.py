"""
Button class
"""
import pygame


class ImageButton():
    """
    Define button class for an image
    """

    def __init__(self, x, y, image_surface, scale):
        """constructor"""

        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        """draw button and handle if clicked or not"""

        action = False
        pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                self.clicked = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action

class FontButton():
    """
    Define button class for a font
    """

    def __init__(self, x, y, font_surface, scale):
        """constructor"""

        width = font_surface.get_width()
        height = font_surface.get_height()
        self.font_surface = pygame.transform.scale(font_surface, (int(width * scale), int(height * scale)))
        self.rect = self.font_surface.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        """draw button and handle if clicked or not"""

        action = False
        pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                self.clicked = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action