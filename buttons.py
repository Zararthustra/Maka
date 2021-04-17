"""
Button module for operators and nums
"""
import pygame
from sounds import current_op_sound, current_num_sound


pygame.init()


class OpButton():
    """
    Define button class for an image
    """

    def __init__(self, x, y, neutral_surface, clicked_surface, scale):
        """constructor"""
        width = neutral_surface.get_width()
        height = neutral_surface.get_height()
        self.image = pygame.transform.scale(neutral_surface, (int(width * scale), int(height * scale)))
        self.clicked_image = pygame.transform.scale(clicked_surface, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw_check_click(self, surface):
        """draw button and handle if clicked or not"""
        from main import CURRENT_OP
        action = False
        pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                self.clicked = True
                current_op_sound.play()
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        if CURRENT_OP and CURRENT_OP == self:
            surface.blit(self.clicked_image, (self.rect.x, self.rect.y))
        else:
            surface.blit(self.image, (self.rect.x, self.rect.y))

        return action


class NumButton(pygame.sprite.Sprite):
    """
    Define button class for nums
    """
    
    load_font = pygame.font.Font('The_good_count/assets/MAGNETOB.TTF', 120)

    def __init__(self, x, y, num):
        """Constructor"""
        super().__init__()
        
        self.num = num
        self.x = x
        self.y = y
        self.clicked = False

    def get_clicked(self):
        """Check if button is clicked or not"""

        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                current_num_sound.play()
                return self.clicked
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
            return self.clicked

    def update(self):
        from main import CURRENT_NUM
        """Update surface when the number has changed"""
        
        if self.clicked:
            font_surface = self.load_font.render(str(self.num), False, (200, 200, 200))
        elif CURRENT_NUM and CURRENT_NUM == self:
            font_surface = self.load_font.render(str(self.num), False, (30, 30, 50))
        else:
            font_surface = self.load_font.render(str(self.num), False, (100, 100, 100))


        width = font_surface.get_width()
        height = font_surface.get_height()

        self.image = pygame.transform.scale(font_surface, (int(width), int(height)))
        self.rect = self.image.get_rect(center = (self.x, self.y))