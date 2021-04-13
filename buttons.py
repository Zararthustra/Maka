"""
Button class
"""
import pygame
pygame.init()


class OpButton():
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

    def draw_check_click(self, surface):
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


class NumButton(pygame.sprite.Sprite):
    """
    Define button class for nums
    """

    def __init__(self, x, y, num):
        """Constructor"""
        super().__init__()
        
        self.num = num
        self.x = x
        self.y = y
        self.xreset = x
        self.yreset = y
        self.clicked = False

    def get_clicked(self):
        """Check if button is clicked or not"""

        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                return self.clicked
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
            return self.clicked

    def update(self):
        """Update surface when the number has changed"""
        load_font = pygame.font.Font('Maka/assets/MAGNETOB.TTF', 120)
        font_surface = load_font.render(str(self.num), False, (255, 0, 0))
        width = font_surface.get_width()
        height = font_surface.get_height()

        self.image = pygame.transform.scale(font_surface, (int(width), int(height)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)

    def reset(self):
        """Reset position of current num"""
        self.x = self.xreset
        self.y = self.yreset