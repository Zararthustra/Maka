"""
Button class
"""
import pygame

pygame.init()

class ImageButton():
    """
    Define button class for an image
    """

    def __init__(self, x, y, image_surface, scale):
        """constructor"""

        width = image_surface.get_width()
        height = image_surface.get_height()
        self.image = pygame.transform.scale(image_surface, (int(width * scale), int(height * scale)))
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

FONT = pygame.font.Font('Maka/assets/MAGNETOB.TTF', 120)

class FontButton():
    """
    Define button class for a font
    """
    def __init__(self, x, y, num, scale):
        """constructor"""

        self.num = num
        self.surface = FONT.render(str(self.num), False, (255, 0, 0))
        width = self.surface.get_width()
        height = self.surface.get_height()
        self.scaled = pygame.transform.scale(self.surface, (int(width * scale), int(height * scale)))
        self.rect = self.scaled.get_rect()
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
        surface.blit(self.scaled, (self.rect.x, self.rect.y))

        return action